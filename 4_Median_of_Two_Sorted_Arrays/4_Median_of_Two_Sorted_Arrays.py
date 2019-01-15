class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length % 2 == 0:  # even list
            e1 = self.quickSelect(nums1 + nums2, length // 2)
            #print(nums1, nums2, e1, length//2)
            e2 = self.quickSelect(nums1 + nums2, length//2 - 1)
            #print(nums1, nums2, e2, length//2 - 1)
            ans = (e1 + e2) / 2
        else:  # odd list
            ans = self.quickSelect(nums1 + nums2, length // 2)
        return ans
    
    def quickSelect(self, nums, index):
        length = len(nums)
        median = nums[length-1]
        #print(nums)
        i = 0
        j = length - 1
        while i < j:  # until pointers meet
            while nums[i] <= median and i < j:  # stop when greater than or equal to median
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
            while nums[j] >= median and i < j:  # stop when less or equal than median
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        #print(nums, median, i, index)
        res = 0
        if index < i:  # recurse in smaller list
            res = self.quickSelect(nums[:i], index)
        elif index > i:  # recurse in greater list
            res = self.quickSelect(nums[i+1:], index - i-1)
        else:
            res = median
        return res
