class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # in-place partition like method
        idx = 0  # processed index
        for i in range(len(nums)):
            if nums[i] != val:  # not the target
                nums[idx] = nums[i]
                idx += 1
        return idx
