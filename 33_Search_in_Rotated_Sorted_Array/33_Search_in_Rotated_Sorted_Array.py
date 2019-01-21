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
        middle = (low + high) // 2
        if nums[middle] != target:
            left = self.search(nums[low:middle], target)
            right = self.search(nums[middle+1:high+1], target)
            if left != -1:
                return low + left
            elif right != -1:
                return middle+1+right
            else:  # no find
                return -1
        else:
            return middle
