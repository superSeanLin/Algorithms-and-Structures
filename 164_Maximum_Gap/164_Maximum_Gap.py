class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## use Radix Sort, O(kN), k is the length of the digit
        n = len(nums)
        if n < 2:
            return 0
        nums = self.radixSort(nums)
        gap = 0
        for i in range(n-1):
            diff = nums[i+1] - nums[i]
            if diff > gap:
                gap = diff
        return gap
    
    def radixSort(self, nums):
        bucket = [[] for i in range(10)]  # intermediate buckets
        dev = 1
        m = max(nums)
        while m // dev > 0:
            for e in nums:
                bucket[(e//dev)%10].append(e)
            nums = []
            for each in bucket:
                nums.extend(each)
            bucket = [[] for i in range(10)]
            dev *= 10
        return nums
