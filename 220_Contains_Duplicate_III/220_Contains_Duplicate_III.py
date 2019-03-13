class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # keep buckets list, separate by t+1 -> same quotient means diff <= w; O(n)
        # also build a BST for next K
        if t < 0:
            return False
        n = len(nums)
        d = {}  # buckets
        w = t + 1
        for i in range(n):
            m = nums[i] // w  # quotient
            if m in d:  # same quotient, abs(diff) must <= w
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:    # adjacent bucket is also possible
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i - k] // w]  # keep k elements in d
        return False

        
