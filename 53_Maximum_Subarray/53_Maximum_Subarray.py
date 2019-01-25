class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## use DP
        n = len(nums)
        s = [0] * n
        s[-1] = nums[-1]
        maximum = nums[-1]
        for i in range(n-2, -1, -1):
            s[i] = max(nums[i], nums[i]+s[i+1])
            if s[i] > maximum:
                maximum = s[i]
        return maximum
