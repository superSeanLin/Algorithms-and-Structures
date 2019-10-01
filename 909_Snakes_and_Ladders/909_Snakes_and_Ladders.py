from heapq import *
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # use BFS
        n = len(board)
        queue = []  #  (step, index)
        heappush(queue, (0, 0))
        visited = set()  # if reach before, then previous is smaller
        while queue:
            (step, index) = heappop(queue)
            if index == n*n-1:  # reach the destination
                return step
            nxt = index+1
            while nxt <= index+6 and nxt <= n*n-1:
                temp = nxt
                x, y = self.index2coor(nxt, n)
                if board[x][y] != -1:
                    temp = board[x][y]-1
                if temp not in visited:
                    visited.add(temp)
                    heappush(queue, (step+1, temp))
                nxt += 1
        return -1
        
    
    def index2coor(self, idx, n):
        row = idx // n
        offset = idx - (row * n)
        if row % 2 == 1:  # left -> right, decrease
            col = n - offset - 1
        else:  # left -> right, increase
            col = offset
        row = n - row - 1
        return row, col
    
    # def coor2index(self, row, col, n):
    #     idx = (n-row-1) * n
    #     if (row % 2 == 0 and n % 2 == 0) or (row % 2 == 1 and n % 2 == 1): # left -> right, decrease
    #         return idx + (n - col) - 1
    #     else:  # left -> right, increase
    #         return idx + col
