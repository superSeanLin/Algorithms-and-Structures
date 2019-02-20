class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## method 1: get last bit
        # count = 0
        # for i in range(32):
        #     last = n & 1
        #     if last:
        #         count += 1
        #     n = n >> 1
        # return count
        
        ## method 2: n & n-1 will flip the least significant 1
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count
            
