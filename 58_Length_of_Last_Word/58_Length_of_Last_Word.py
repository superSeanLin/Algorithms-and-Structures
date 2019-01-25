class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = 0
        previous = 0
        n = len(s)
        for i in range(n):
            curr += 1
            if s[i] == ' ':
                if curr-1:
                    previous = curr - 1
                curr = 0
        if curr:
            return curr
        else:
            return previous 
