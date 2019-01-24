import copy
class Solution:
    def __init__(self):
        self.ans = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ## use constraints propagation, O(n^3); Also can randomly set and then, hill-climbing to quickly get one single solution
        avail = []
        for i in range(n):
            avail.append(list(range(n)))  # each line with available index
        row1 = 0
        for col1 in range(n):
            temp = copy.deepcopy(avail)
            self.setAndCheck(row1, col1, temp)
        return self.ans
    
    def setAndCheck(self, row, col, avail):
        n = len(avail)
        avail[row] = [col]
        if row == n-1:
            # valid solution
            self.ans.append(self.buildSolution(avail))
            return True
        # first reset constraints matrix
        for row2 in range(row+1, n):
            if col in avail[row2]:
                avail[row2].remove(col)
            for col2 in range(n):
                if col2 in avail[row2] and abs(col2 - col) / abs(row2 - row) == 1:  # diagonal line
                    avail[row2].remove(col2)
            if len(avail[row2]) == 0:  # no valid value
                return False
        # then DFS
        b = False
        for row2 in range(row+1, n):
            for col2 in avail[row2]:
                temp = copy.deepcopy(avail)
                if not self.setAndCheck(row2, col2, temp):  # no need for next row
                    b = True
            if b:
                break
        return False
    
    def buildSolution(self, matrix):
        #print(matrix)
        res = []
        n = len(matrix)
        for m in matrix:
            idx = m[0]
            line = ""
            for i in range(n):
                if i == idx:
                    line += 'Q'
                else:
                    line += '.'
            res.append(line)
        return res
