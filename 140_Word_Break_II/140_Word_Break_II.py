class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        res = self.dp(s, wordDict)
        return res
    
    def dp(self, s, wordDict):
        n = len(s)
        seg = [False] * (n+1)
        seg[-1] = True
        pos = [[] for i in range(n+1)]  # store valid position
        pos[-1] = [-1]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict and seg[j]:
                    seg[i] = True
                    pos[i].append(j)
        res = []
        self.backTrace(s, pos, 0, [], res)
        return res
    
    def backTrace(self, s, pos, start, path, res):  # DFS
        nxt = pos[start]
        if nxt == [-1]:  # stop
            res.append(" ".join(path))
            return
        for end in nxt:
            path.append(s[start : end])
            self.backTrace(s, pos, end, path, res)
            path.pop()
