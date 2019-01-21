class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # naive solution must work; maybe use constraint propagation (AC-3) but should be slow and memory consuming here
        seen = set()
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
                elif (i, cell) in seen or (cell, j) in seen or (i//3, j//3, cell) in seen:  # seen value
                    return False
                seen.add((i, cell))
                seen.add((cell, j))
                seen.add((i//3, j//3, cell))
        return True
