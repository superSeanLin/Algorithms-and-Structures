class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        ## a XOR a = 0; a XOR 0 = a
        res = 0
        for i in nums:
            res ^= i
        return res
