class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 2:
            return 0
        min_sum = target + 1000
        nums = self.quickSort(nums)
        for i in range(len(nums)):  # fix first element
            j = i+1
            k = len(nums)-1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > target:  # too large
                    k -= 1
                elif curr_sum < target:  # too small
                    j += 1
                else:  # find exactly sum
                    return target
                distance = abs(curr_sum - target)
                if distance < abs(min_sum - target):
                    min_sum = curr_sum
        return min_sum
            
    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[-1]  # set last element as pivot
        idx, nums = self.partition(nums, pivot)
        left = self.quickSort(nums[:idx])
        right = self.quickSort(nums[idx+1:])
        return left + [pivot] + right
    
    def partition(self, nums, pivot):
        # in-place partition
        idx = 0  # sorted index
        for i in range(len(nums)-1):
            if idx <= i and nums[i] < pivot:  # find a smaller element
                nums[idx], nums[i] = nums[i], nums[idx]  # swap i and idx
                idx += 1
        nums[idx], nums[-1] = nums[-1], nums[idx]  # nums[idx] greater than or equal to pivot
        return idx, nums
                    
