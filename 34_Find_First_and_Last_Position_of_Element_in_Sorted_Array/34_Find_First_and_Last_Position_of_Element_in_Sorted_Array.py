class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0:
            return [-1, -1]
        low = 0
        high = len(nums)-1
        return self.binarySearch(nums, low, high, target)

    def binarySearch(self, nums, low, high, target):
        if low > high:
            return [-1, -1]
        middle = (low + high) // 2
        if nums[middle] < target:
            return self.binarySearch(nums, middle+1, high, target)
        elif nums[middle] > target:
            return self.binarySearch(nums, low, middle-1, target)
        else:  # nums[middle] == targte
            left = self.binarySearch(nums, low, middle-1, target)
            right = self.binarySearch(nums, middle+1, high, target)
            l, r = left[0], right[1]
            if l == -1:
                l = middle
            if r == -1:
                r = middle
            return [l, r]
