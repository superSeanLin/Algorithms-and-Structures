class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ## can use 2Sum twice; first, find all sum of 2 distinct numbers; then find if two sums can reach the target
        if len(nums) <= 3:
            return []
        nums = self.quickSort(nums)
        res = []
        for i in range(len(nums)):  # fix first element
            for j in range(i+1, len(nums)):  # fix second element
                # Note: binary search is not direct here
                low = j+1
                high = len(nums) - 1
                while low < high:
                    distance = nums[i] + nums[j] + nums[low] + nums[high] - target
                    if distance > 0:  # too large
                        high -= 1
                    elif distance < 0:  # too small
                        low += 1
                    else:  # find solution
                        temp = [nums[i], nums[j], nums[low], nums[high]]
                        if temp not in res:
                            res.append(temp)
                        low += 1
        return res
    
    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[-1]  # set last element as pivot
        left, right = self.partition(nums, pivot)
        return self.quickSort(left) + [pivot] + self.quickSort(right)
                    
    def partition(self, nums, pivot):
        idx = 0  # sorted index
        for i in range(len(nums)-1):  # last one is the pivot
            if idx <= i and nums[i] < pivot:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[-1] = nums[-1], nums[idx]
        return nums[:idx], nums[idx+1:]
