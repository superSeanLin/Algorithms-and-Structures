class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ## O(1) space method: traverse the matrix, meet 0 then set matrix[i][0], matrix[0][j] to be 0 (they will not be checked again), finally traverse again to set 0
        row = set()
        col = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for j in col:
            for i in range(m):
                matrix[i][j] = 0
        
        
