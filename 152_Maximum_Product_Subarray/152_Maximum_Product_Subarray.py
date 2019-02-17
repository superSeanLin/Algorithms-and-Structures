class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## recurse; O(n) method, accumulate from left to right, and then right to left, meet 0 then reset
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        index = []  # store negative index
        zeros = []  # store zero index
        for i, e in enumerate(nums):
            if e < 0:
                index.append(i)
            if e == 0:
                zeros.append(i)
        if zeros:  # first separated by zeros
            product = max(0, self.maxProduct(nums[:zeros[0]]), self.maxProduct(nums[zeros[-1]+1:]))
            if len(zeros) > 1:
                for i in range(len(zeros)-1):
                    product = max(product, self.maxProduct(nums[zeros[i]+1:zeros[i+1]]))
            return product
        if len(index) % 2 == 0:  # even negative
            return reduce(lambda a, b: a*b, nums, 1)
        else:  # odd negative
            return max(self.maxProduct(nums[:index[-1]]), self.maxProduct(nums[index[0]+1:]))
        
