class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # naive solution
        # first find number of non positive
        counter = 0
        for x in nums:
            if x <= 0:
                counter += 1
        # then find the minimum
        minimum = 2**31-1
        for x in nums:
            if x > 0 and x < minimum:
                minimum = x
        if minimum == 2**31-1:
            minimum = 0
        elif minimum > 1:
            return 1
        # finially find the missing positive
        i = 1
        while i < len(nums) - counter:
            if minimum+i not in nums:
                return minimum+i
            i += 1
        return minimum+i
            
        
