class Solution:
    ## use DP to speed up
    def numTrees(self, n: 'int') -> 'int':
        uniqueBST = [[0] * n for i in range(n)]  # return [0, n-1]
        for i in range(n):
            for j in range(n):
                if i >= j:
                    uniqueBST[i][j] = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                temp = 0
                for k in range(i+1, j):
                    temp += uniqueBST[i][k-1] * uniqueBST[k+1][j]
                uniqueBST[i][j] += temp
                uniqueBST[i][j] += uniqueBST[i+1][j]  # only left
                uniqueBST[i][j] += uniqueBST[i][j-1]  # only right
        return uniqueBST[0][n-1]
