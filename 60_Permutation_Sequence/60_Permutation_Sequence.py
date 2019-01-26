import math
class Solution:
    def __init__(self):
        self.seq = None
        
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ## O(n) to compute factorial; use the nextPermutation is way too slow; Actually compute the factorial
        if not self.seq:  # initialize
            self.seq = list(range(1, n+1))
        res = ""
        num = math.factorial(n-1)
        mul = (k-1) // num
        if k == 1:
            return "".join([str(c) for c in self.seq])
        if mul == n:  # last one
            self.seq = seq[::-1]
            return "".join([str(c) for c in self.seq])
        elif mul >= 0:
            leading = self.seq[mul]
            self.seq.pop(mul)
            res += str(leading) + self.getPermutation(n-1, k - mul*num)
        return res
