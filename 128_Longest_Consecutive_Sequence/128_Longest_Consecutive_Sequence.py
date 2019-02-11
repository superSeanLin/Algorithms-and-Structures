class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        ## idea from positive consecutive sequence, but take too much space
        ## use hashtable
        s = set(nums)
        maximum = 0
        for i in s:
            if not i-1 in s:  # find the smallest one of each sequence
                curr = i
                count = 1
                while curr+1 in s:
                    count += 1
                    curr += 1
                maximum = max(maximum, count)
        return maximum
                
