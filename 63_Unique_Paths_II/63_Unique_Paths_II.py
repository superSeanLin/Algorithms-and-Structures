class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ## use DP
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path = [[0] * n for _ in range(m)]
        if obstacleGrid[m-1][n-1]:
            path[m-1][n-1] = 0
        else:
            path[m-1][n-1] = 1
        for i in range(m-2, -1, -1):
            if not obstacleGrid[i][n-1]:  # no obstacle
                path[i][n-1] = path[i+1][n-1]
            else:
                path[i][n-1] = 0
        for j in range(n-2, -1, -1):
            if not obstacleGrid[m-1][j]:
                path[m-1][j] = path[m-1][j+1]
            else:
                path[m-1][j] = 0
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j]:   # obstacle
                    path[i][j] = 0
                else:
                    path[i][j] = path[i+1][j] + path[i][j+1]
        return path[0][0]
        
