class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # sliding window, O(n)
        n = len(nums)
        if not n or sum(nums) < s:
            return 0
        start, end = 0, 0
        minimum = n
        curr = nums[0]
        while start < n:
            while curr < s and end < n-1:  # until window sum >= s
                end += 1
                curr += nums[end]
            minimum = min(end - start + 1, minimum)
            while curr >= s and start < n:  # unitil window sum < s
                minimum = min(end - start + 1, minimum)
                curr -= nums[start]
                start += 1
            if start == n-1 or end == n-1:  # not possible afterwards
                break
        return minimum
    
        ## recursive method
        # curr = sum(nums)
        # n = len(nums)
        # if not n or curr < s:
        #     return 0
        # if curr == s:
        #     return n
        # elif curr > s:
        #     left = self.minSubArrayLen(s, nums[1:])
        #     right = self.minSubArrayLen(s, nums[:-1])
        #     if left == 0 and right == 0:
        #         return n
        #     elif left == 0:
        #         return right
        #     elif right == 0:
        #         return left
        #     else:  # no 0
        #         return min(left, right)
