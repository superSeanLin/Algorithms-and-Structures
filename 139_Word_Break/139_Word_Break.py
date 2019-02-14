class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ## bottom-top DP; O(n^2)
        wordDict = set(wordDict)
        return self.dp(s, wordDict)
    
    def dp(self, s, wordDict):  # phraseDict store valid phrase after
        n = len(s)
        seg = [False] * (n+1)  # see if s[i:] in wordDict
        seg[-1] = True  # for empty string
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict:
                    seg[i] = seg[i] or seg[j]
                if seg[i]:
                    break
        return seg[0]
        
