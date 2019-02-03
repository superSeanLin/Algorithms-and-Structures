class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ## DFS
        if not word:
            return True
        helper = {}  # store char:[index]
        n = len(board)
        if not n:
            return False
        m = len(board[0])
        if not m:
            return False
        for i in range(n):
            for j in range(m):
                char = board[i][j]
                if not char in helper:
                    helper[char] = [(i,j)]
                else:
                    helper[char].append((i,j))
        return self.exist2(board, word, helper, [])
        
    def exist2(self, board, word, helper, path):
        if not word:
            return True
        char = word[0]
        if not char in helper:
            return False
        else:
            for coord in helper[char]:
                if not path:
                    temp = path + [coord]
                    if self.exist2(board, word[1:], helper, temp):
                        return True
                elif (not coord in path) and self.isNeighbor(coord, path[-1]):
                    temp = path + [coord]
                    if self.exist2(board, word[1:], helper, temp):
                        return True
        return False
    
    def isNeighbor(self, coord, current):  # self excluded
        (x1, y1) = coord
        (x2, y2) = current
        if abs(x1 - x2) + abs(y1 - y2) == 1:
            return True
        else:
            return False
                
