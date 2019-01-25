class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## DP, O(n^2); check O(n) Greedy algorithm later
        n = len(nums)
        step = [False] * n
        step[-1] = True
        for i in range(n-2, -1, -1):
            if nums[i] + i >= n-1:  # can direct reach
                step[i] = True
                continue
            for j in range(i+nums[i], i, -1):  # j stay in valid range
                if step[j]:
                    step[i] = True
        return step[0]
                
