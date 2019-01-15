class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        if x < 0:
            negative = -1
            x *= -1
        x = str(x)[::-1]
        x = int(x)
        if x > 2**31 - 1 or x < -2**31:
            x = 0
        return x * negative
        
