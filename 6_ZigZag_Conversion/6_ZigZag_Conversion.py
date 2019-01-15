class Solution:
    ## append char to each line string directly
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= 1:
            return s
        z = [''] * numRows
        r = 2 * numRows - 2  ## one round has r chars
        for i in range(len(s)):
            index = i // r
            row = i % r
            if row > numRows-1:
                row = r - row
            z[row] += s[i]
        res = z[0]
        for i in range(1, numRows):
            res = res + z[i]
        return res
