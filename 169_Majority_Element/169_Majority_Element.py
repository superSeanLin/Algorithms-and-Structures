class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums = self.quickSort(nums)
        nums.sort()
        return nums[len(nums)//2]  # must incurr here
        
    def quickSort(self, nums):
        ## in-place quickSort
        if not nums:
            return []
        idx, nums = self.partition(nums)
        left = self.quickSort(nums[:idx])
        right = self.quickSort(nums[idx+1:])
        return left + [nums[idx]] + right
    
    def partition(self, nums):
        pivot = nums[-1]
        idx = 0  # processed index
        for i in range(len(nums)):
            if nums[i] < pivot:
                nums[idx], nums[i] = nums[i], nums[idx]  # allocate new memory for nums; hard to change in-place
                idx += 1
        nums[idx], nums[-1] = nums[-1], nums[idx]
        return idx, nums
        
