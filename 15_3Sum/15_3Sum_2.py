class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## use two point, O(n^2)
        res = []
        nums.sort()
        prev = None  # avoid duplicate
        n = len(nums)
        for i in range(n):
            if nums[i] == prev:
                continue
            j, k = i+1, n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            prev = nums[i]
        return res
