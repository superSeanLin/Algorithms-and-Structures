class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ## use DP
        path = [[0] * n for _ in range(m)]
        path[m-1][n-1] = 1
        for i in range(m-2, -1, -1):  # base case
            path[i][n-1] = 1
        for j in range(n-2, -1, -1):
            path[m-1][j] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                path[i][j] = path[i+1][j] + path[i][j+1]
        return path[0][0]
