class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        idx = m + n - 1  # start from bottom
        i, j = m-1, n-1
        while idx >= 0 and i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
                idx -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
                idx -= 1
        if i < 0:
            while j >= 0:
                nums1[idx] = nums2[j]
                j -= 1
                idx -= 1
        elif j < 0:
            while i >= 0:
                nums1[idx] = nums1[i]
                i -= 1
                idx -= 1
        
