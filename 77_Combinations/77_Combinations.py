class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if k == 0:
            return [[]]
        for i in range(n, 0, -1):
            if k == 1:
                res.append([i])
            else:
                temp = self.combine(i-1, k-1)
                for t in temp:
                    res.append([i] + t)
        return res        
