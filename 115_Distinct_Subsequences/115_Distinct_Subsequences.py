class Solution:
    def numDistinct(self, s: 'str', t: 'str') -> 'int':
        ## use DP
        m = len(s)
        if m == 0:
            return 0
        n = len(t)
        if n == 0:
            return 1
        sub = [[0]*m for i in range(n)]  # sub(i,j) = number of t[j:] in s[i:]
        if s[-1] == t[-1]:
            sub[n-1][m-1] = 1
        for j in range(m-2, -1, -1):  # base case for the single char
            if s[j] == t[-1]:
                sub[n-1][j] = 1 + sub[n-1][j+1]
            else:
                sub[n-1][j] = sub[n-1][j+1]
        for i in range(n-2, -1, -1):
            for j in range(m-n+i, -1, -1):  # start with same possible length
                sub[i][j] = sub[i][j+1]  # keep prev result
                if s[j] == t[i]:
                    sub[i][j] += sub[i+1][j+1]
        return sub[0][0]
