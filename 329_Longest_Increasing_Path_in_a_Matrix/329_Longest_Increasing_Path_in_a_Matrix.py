class Solution:
    def __init__(self):
        # self.maxi = 0
        self.memo = {}  # (index of start) : the length of the longest increasing path; since there is no overlap
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # start with dfs; maybe use memoization to store afterwards
        # O(mn) time complexity since only check each for one time
        n = len(matrix)
        if not n:
            return 0
        m = len(matrix[0])
        if not m:
            return 0
        maxi = 0
        for i in range(n):
            for j in range(m):
                maxi = max(maxi, self.dfs(matrix, i, j))
        return maxi
    
    def dfs(self, matrix, i, j):
        n, m = len(matrix), len(matrix[0])
        curr = matrix[i][j]
        maxi = 0
        # left
        if i-1 >= 0 and matrix[i-1][j] > curr:
            if (i-1, j) in self.memo:  # seen before
                maxi = max(maxi, self.memo[(i-1, j)])
            else:
                maxi = max(maxi, self.dfs(matrix, i-1, j))
        # right
        if i+1 < n and matrix[i+1][j] > curr:
            if (i+1, j) in self.memo:  # seen before
                maxi = max(maxi, self.memo[(i+1, j)])
            else:
                maxi = max(maxi, self.dfs(matrix, i+1, j))
        # up
        if j-1 >= 0 and matrix[i][j-1] > curr:
            if (i, j-1) in self.memo:  # seen before
                maxi = max(maxi, self.memo[(i, j-1)])
            else:
                maxi = max(maxi, self.dfs(matrix, i, j-1))
        # down
        if j+1 < m and matrix[i][j+1] > curr:
            if (i, j+1) in self.memo:  # seen before
                maxi = max(maxi, self.memo[(i, j+1)])
            else:
                maxi = max(maxi, self.dfs(matrix, i, j+1))
        self.memo[(i, j)] = maxi+1
        return maxi+1
        
