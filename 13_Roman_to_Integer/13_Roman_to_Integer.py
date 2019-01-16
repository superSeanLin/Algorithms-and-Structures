class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use dict to gain faster solution
        i, v, x, l, c, d, m = 0, 0, 0, 0, 0, 0, 0
        for idx in range(len(s)):
            if s[idx] == 'M':
                m += 1
            elif s[idx] == 'D':
                d += 1
            elif s[idx] == 'C':
                if idx+1 < len(s) and s[idx+1] in ('M', 'D'):
                    c -= 1
                else:
                    c += 1
            elif s[idx] == 'L':
                l += 1
            elif s[idx] == 'X':
                if idx+1 < len(s) and s[idx+1] in ('C', 'L'):
                    x -= 1
                else:
                    x += 1
            elif s[idx] == 'V':
                v += 1
            elif s[idx] == 'I':
                if idx+1 < len(s) and s[idx+1] in ('X', 'V'):
                    i -= 1
                else:
                    i += 1
        print(i, v, x, l, c, d, m)
        return (i + 5*v + 10*x + 50*l + 100*c + 500*d + 1000*m)
