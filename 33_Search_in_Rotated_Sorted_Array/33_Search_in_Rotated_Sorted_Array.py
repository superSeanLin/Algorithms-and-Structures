class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## bitonic sequence
        ## also can find smallest/largest through Binary search and then do binary search again
        if len(nums) <= 0:
            return -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
