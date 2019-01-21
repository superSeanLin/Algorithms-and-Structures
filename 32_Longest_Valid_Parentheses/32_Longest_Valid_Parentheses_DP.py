class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## use DP
        if len(s) == 0:
            return 0
        lvp = [0] * len(s)  # list of longest length starting from index i
        if s[len(s)-2] == '(' and s[len(s)-1] == ')':
            lvp[len(s)-2] = 2
        for i in range(len(s)-3, -1, -1):  # from bottom to top; ignore ')'
            if s[i] == '(' and s[i+1] == ')':  #()...
                lvp[i] = 2 + lvp[i+2]
            elif i+lvp[i+1]+1 < len(s) and s[i] == '(' and s[i+1] == '(' and s[i + lvp[i+1] + 1] == ')': # ((...))
                lvp[i] = 2 + lvp[i+1]
                if i+lvp[i+1]+2 < len(s):
                    lvp[i] += lvp[i+lvp[i+1]+2]  # also take substring after ')' into consideration
        return max(lvp)
