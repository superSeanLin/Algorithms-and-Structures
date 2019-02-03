class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        ## Need more review
        if len(nums) <= 0:
            return False
        low, high = 0, len(nums)-1
        while low <= high:
            while low < high and nums[low] == nums[high]:  # tricky part
                low += 1
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
