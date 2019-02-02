class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # could use DP to optimize
        res = [[]]
        for i, e in enumerate(nums):
            temp = self.subsets(nums[i+1:])
            for t in temp:
                res.append([e] + t)
        return res
