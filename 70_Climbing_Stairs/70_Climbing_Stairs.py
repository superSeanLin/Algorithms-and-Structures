class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## 1D array DP, or O(1) DP
        path = [0] * n
        path[n-1] = 1
        if n >= 2:
            path[n-2] = 2
        for i in range(n-3, -1, -1):
            path[i] = path[i+1] + path[i+2]
        return path[0]
        
