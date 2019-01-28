class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## DP like; but using multiply is the wrong way
        res = 0
        n = len(s)
        decoder = [0] * (n+1)  # store possible way to represent s[:i]
        decoder[0] = 1
        for i in range(1, n+1):
            if s[i-1] != '0':
                decoder[i] += decoder[i-1]  # leave s[i-1] alone and accumulate
            if i > 1 and int(s[i-2:i]) > 9 and int(s[i-2:i]) < 27:
                decoder[i] += decoder[i-2]  # put s[i-2] and s[i-1] together
        return decoder[n]
