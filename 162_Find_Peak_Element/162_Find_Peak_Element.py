class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == n-1 or nums[mid+1] < nums[mid]):  # index out of range
                return mid
            elif (mid == 0 or nums[mid-1] < nums[mid]) and (mid == n-1 or nums[mid] < nums[mid+1]):
                low = mid + 1
            elif (mid == 0 or nums[mid-1] > nums[mid]) and (mid == n-1 or nums[mid] > nums[mid+1]):
                high = mid - 1
            else:  # nums[mid] smallest
                low = mid + 1
