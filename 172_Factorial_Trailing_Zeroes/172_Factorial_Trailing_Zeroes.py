import math
class Solution:
    ## see how many pairs of 2 and 5; since #2 >> #5, so focus on #5
    def trailingZeroes(self, n: 'int') -> 'int':
        if n < 5:
            return 0
        return (n//5 + self.trailingZeroes(n//5))

        
