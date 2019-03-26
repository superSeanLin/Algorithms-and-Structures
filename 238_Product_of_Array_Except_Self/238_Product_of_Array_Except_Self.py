class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## 135 candy like
        n = len(nums)
        omit = [1] * n
        p = 1
        # omit ith and store left product
        for i in range(n):
            omit[i] = p
            p *= nums[i]
        p = 1
        # omit ith and store right product
        for i in range(n-1, -1, -1):
            omit[i] *= p
            p *= nums[i]
        return omit
