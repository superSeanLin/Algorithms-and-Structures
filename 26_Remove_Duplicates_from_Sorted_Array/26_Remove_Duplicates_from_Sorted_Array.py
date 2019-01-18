class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = list(set(nums))  # Note: redirect nums pointer to a new allocation, will not work
        # use in-place partition like method
        if len(nums) == 0:  # empty list
            return 0
        idx = 0  # processed index
        for i in range(len(nums)):
            if nums[i] != nums[idx]:  # new digit
                idx += 1
                nums[idx] = nums[i]
        return idx+1
