class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ## Knuth-Morris-Pratt algorithm
        pi = self.computePI(p)
        k = -1  # index of matched char
        for i in range(len(s)):  # scan the text
            while k > -1 and p[k+1] != s[i]:  # next char does not match
                k = pi[k]
            if p[k+1] == s[i]:
                k = k + 1  # next char matches
            if k == len(p)-1:  # match all pattern
                return True
        return False
    
    def computePI(self, p):
        length = len(p)
        pi = [0] * length  # index of start of longest prefix array
        pi[0] = -1  # first one have no repeat prefix
        k = -1
        for i in range(1, length):
            while k > -1 and p[k+1] != p[i]:  # until k = -1 or find a commom prefix
                k = pi[k]
            if p[k+1] == p[i]:
                k = k + 1
            pi[i] = k
        return pi
        
