class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # recurse, case without '*' will be straight forward
        # use DP to speed up
        len_s = len(s)
        len_p = len(p)
        m = [[False] * (len_p+1) for i in range(len_s+1)]  # 2D array, if s[i:] match with p[j:]
        for i in range(len_s+1):
            j = len_p
            m[i][j] = not s[i:]
        for j in range(len_p-1, -1, -1):
            i = len_s
            m[i][j] = (p[j] == '*') and m[i][j+1]
        # if not p:
        #     return not s
        # if p[0] == '*':
        #     if len(p) > 1:
        #         return self.isMatch(s, p[1:]) or (bool(s) and self.isMatch(s[1:], p))
        #     else:
        #         return True  # '*' can match any sequence
        # else:  # case without '*'
        #     first_match = bool(s) and (s[0] == p[0] or p[0] == '?')
        #     return first_match and self.isMatch(s[1:], p[1:])
        for j in range(len_p-1, -1, -1):
            for i in range(len_s-1, -1, -1):
                if p[j] == '*':
                    if len(p[j:]) > 1:
                        m[i][j] = m[i][j+1] or (bool(s[i:]) and m[i+1][j])
                    else:
                        m[i][j] = True
                else:
                    first_match = bool(s[i:]) and (s[i] == p[j] or p[j] == '?')
                    m[i][j] = first_match and m[i+1][j+1]
        return m[0][0]
