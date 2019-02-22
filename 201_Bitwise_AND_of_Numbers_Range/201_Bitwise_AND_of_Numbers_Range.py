import math
class Solution:
    def rangeBitwiseAnd(self, m: 'int', n: 'int') -> 'int':
        if m == 0 or m == n:
            return m
        a = int(math.log(n, 2))  # n = 2**a + x
        b = int(math.log(m, 2))  # m = 2**b + y
        if a > b:  # different range
            return 0
        return 2**a + self.rangeBitwiseAnd(m&(2**a-1), n&(2**a-1))  # a == b; m&(2**a-1) == m - 2**a-1
