class Solution:
    def __init__(self):
        self.unSurr = set()

    def solve(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        ## DFS and use a hashset to keep
        ## faster idea: start from border and seek unsurrounded
        m = len(board)
        if not m:
            return
        n = len(board[0])
        if not n:
            return
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and self.surrounded(i, j, visited, board):
                    board[i][j] = 'X'

    def onBorder(self, x, y, m, n):
        if x in (0, m-1) or y in (0, n-1):
            return True
        return False
    
    def surrounded(self, x, y, visited, board):
        m = len(board)
        n = len(board[0])
        # on boarder checked
        if board[x][y] == 'X' or (x, y) in visited:
            return True
        if (x, y) in self.unSurr or self.onBorder(x, y, m, n) :
            return False
        # up, down, left, right = (x-1, y), (x+1, y), (x, y-1), (x, y+1)
        visited.add((x, y))  # avoid copy, save space
        if self.surrounded(x-1, y, visited, board) and self.surrounded(x+1, y, visited, board) \
        and self.surrounded(x, y-1, visited, board) and self.surrounded(x, y+1, visited, board):
            return True
        self.unSurr.add((x, y))
        visited.clear()
        return False
