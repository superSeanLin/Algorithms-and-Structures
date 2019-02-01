class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## quickSort partition like, Dutch National Flag
        n = len(nums)
        idx, idx1, idx2 = 0, 0, n-1  # processed index for 0, 1, 2; idx points to end of 0 and start of 1w
        while idx1 <= idx2:
            if nums[idx1] == 0:
                nums[idx1], nums[idx] = nums[idx], nums[idx1]
                idx += 1
                idx1 += 1
            elif nums[idx1] == 1:
                idx1 += 1
            else:
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
                idx2 -= 1
        
