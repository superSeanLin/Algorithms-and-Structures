class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## find the leading number, the farest i->j, i < j; in-place modification
        idx = -1  # farest smaller index
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                idx = i
        if idx > -1:  # find a valid leading number
            # swap with just greater one; the numbers after the leading number are in descending order
            idx2 = idx
            minimum = 2**31-1
            for i in range(idx+1, len(nums)):
                if nums[i] > nums[idx] and nums[i] <= minimum:  # use <= to find last greater element; then do reverse will maintain the ascending order
                    minimum = nums[i]
                    idx2 = i
            nums[idx], nums[idx2] = nums[idx2], nums[idx]
            # reverse the nums after the leading number
            self.MyReverse(nums, idx)
        else:  # no valid solution, return ascending order
            nums.reverse()
    
    def MyReverse(self, nums, idx):
        i = idx+1
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
        
