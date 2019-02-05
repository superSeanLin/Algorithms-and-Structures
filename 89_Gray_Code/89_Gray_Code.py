class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ## xor
        res = []
        for i in range(0, 1<<n):  # n^2
            res.append(i ^ i>>1)  # never notice
        return res
        
