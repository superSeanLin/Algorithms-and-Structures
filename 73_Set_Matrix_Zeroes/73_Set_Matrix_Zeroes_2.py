class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ## O(1) space method: traverse the matrix, meet 0 then set matrix[i][0], matrix[0][j] to be 0 (they will not be checked again), finally traverse again to set 0
        col, row = False, False  # specify if first col and first row should be all 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                col = True
        for j in range(n):
            if matrix[0][j] == 0:
                row = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0] * n
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if col:
            for i in range(m):
                matrix[i][0] = 0
        if row:
            matrix[0] = [0] * n
        return matrix
