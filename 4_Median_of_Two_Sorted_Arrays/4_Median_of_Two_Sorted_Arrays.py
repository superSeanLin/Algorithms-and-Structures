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
    
    def quickSelect(self, nums, index):  # in-place partitionn
        length = len(nums)
        nums[length//2], nums[length-1] = nums[length-1], nums[length//2]  # swap median with the last element
        median = nums[length-1]
        i = 0 # sorted index
        j = 0 # j >= i
        while j < length-1:  # check through the whole list
            if nums[j] < median:
                nums[i], nums[j] = nums[j], nums[i]  # swap nums[i] and nums[j], since nums[i] >= median, nums[j] < median
                i += 1
            j += 1
        nums[length-1], nums[i] = nums[i], nums[length-1]  # i is the final index of median
        res = 0
        if index < i:  # recurse in smaller list
            res = self.quickSelect(nums[:i], index)
        elif index > i:  # recurse in greater list
            res = self.quickSelect(nums[i+1:], index - i-1)
        else:
            res = median
        return res
