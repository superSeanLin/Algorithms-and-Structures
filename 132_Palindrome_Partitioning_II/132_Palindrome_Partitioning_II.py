class Solution:
    ## use DP; O(n^2)
    def minCut(self, s: 'str') -> 'int':
        n = len(s)
        if not n:
            return -1
        # acceleration (base case)
        if s == s[::-1]:
            return 0
        for i in range(1, n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # DP
        cut = [n-1] * (n+1)  # minimum cut on s[i+1:]
        cut[-1] = -1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] == s[i:j][::-1]:
                    cut[i] = min(cut[i], 1+cut[j])
        print(cut)
        return cut[0]
