class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] < target:
            return 1
        if len(nums) == 1 and nums[0] >= target:
            return 0
        low, high = 0, len(nums)-1
        middle = (low + high) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            if nums[middle-1] <= target:
                return middle - (nums[middle-1] == target)
            else:
                return low + self.searchInsert(nums[low:middle], target)
        else:  # nums[middle] < target
            if nums[middle+1] >= target:
                return middle+1
            else:
                return middle+1 + self.searchInsert(nums[middle+1:high+1], target)
