class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # isomorphism, bijection
        res = []
        if not pattern:
            return words
        if not words:
            return res
        n = len(pattern)
        p1 = self.getPattern(pattern)
        for word in words:
            p2 = self.getPattern(word)
            if p1 == p2:
                res.append(word)
        return res
    
    def getPattern(self, pattern):
        order = []
        counter = 0
        visited = {}  # char : counter
        for c in pattern:
            if not c in visited:
                counter += 1
                visited[c] = counter
            order.append(visited[c])
        return "".join([str(e) for e in order])
