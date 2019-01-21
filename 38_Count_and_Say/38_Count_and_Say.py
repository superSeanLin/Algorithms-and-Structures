class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ## Can use DP to speed up
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        res = ""
        i = 0
        while i < len(s):
            count = 0
            previous = s[i]
            while i < len(s) and s[i] == previous:
                count += 1
                i += 1
            res += str(count) + str(previous)
            if i >= len(s):
                return res
        return res
                
        
