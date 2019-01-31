class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ## Use DP
        m = len(grid)
        n = len(grid[0])
        path = [[0]*n for _ in range(m)]
        path[m-1][n-1] = grid[m-1][n-1]
        for i in range(m-2, -1, -1):
            path[i][n-1] = grid[i][n-1] + path[i+1][n-1]
        for j in range(n-2, -1, -1):
            path[m-1][j] = grid[m-1][j] + path[m-1][j+1]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                minimum = min(path[i+1][j], path[i][j+1])
                path[i][j] = grid[i][j] + minimum
        return path[0][0]
        
