class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # one pass DP, O(n), basically calculate the changing point
        if not nums:
            return 0
        n = len(nums)
        up, down = [1]*n, [1]*n  # indicates the length of subsequence if up/down at index i
        for i in range(1, n):
            if nums[i] > nums[i-1]:  # up
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:  # down
                down[i] = up[i-1]+1
                up[i] = up[i-1]
            else:  # equal
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(down[n-1], up[n-1])
            
        ## DP, O(n^2)
        # if not nums:
        #     return 0
        # n = len(nums)
        # pos, neg = [1]*n, [1]*n  # store the length of subsequence where diff between i and i-1 is positive/negative
        # for i in range(1, n):
        #     # positive diff
        #     for j in range(i):
        #         if nums[i] - nums[j] > 0:
        #             pos[i] = max(pos[i], neg[j]+1)
        #     # negative diff
        #     for j in range(i):
        #         if nums[i] - nums[j] < 0:
        #             neg[i] = max(neg[i], pos[j]+1)
        # return max(max(pos), max(neg))
                    
