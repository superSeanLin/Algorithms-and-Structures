class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if not n:
            return n
        k = k % n
        # method 1
        # for i in range(n-k, n):
        #     e = nums.pop()
        #     nums.insert(0, e)
        
        # method 2
        # nums.extend(nums[:n-k])
        # for i in range(n-k):
        #     nums.pop(0)
        
        # method 3
        self.Reverse(nums, n-k, n-1)
        self.Reverse(nums, 0, n-k-1)
        nums.reverse()
    
    def Reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
