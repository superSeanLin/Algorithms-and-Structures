class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        inverse = False
        if n < 0:
            inverse = True
            n *= -1
        res = x
        i = 1
        while i < n and i + i < n:
            res *= res
            i += i
        if i < n:
            res *= self.myPow(x, n-i)
        if inverse:
            res = 1 / res
        return res
        
