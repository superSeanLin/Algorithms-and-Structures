class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # gcd = a*x + b*y; z = k*gcd = k*a*x + k*b*y
        if z > x+y or z < 0:
            return False
        if x > y:
            x, y = y, x
        if x == z or y == z or x+y == z:
            return True
        return z % self.gcd(x,y) == 0
    
    # greatest common divisor
    def gcd(self, x, y):
        while x != 0:
            r = y % x
            y = x
            x = r
        return y
