class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # very tricky solution
        length = len(nums)
        if length == 0:
            return 1
        left = 0
        right = length - 1
        while left <= right:  # make left 1 ~ length (all possible postive numbers in length)
            if nums[left] <= 0 or nums[left] > length:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        # then use left to indicate which number is missing
        for i in range(left):
            visit = abs(nums[i])-1
            if nums[visit] > 0:  # if digit missing, then nums[digit-1] will be positive
                nums[visit] *= -1  # left = -length+1 ~ 0
        # then find postive index
        i = 0
        while i < left:
            if nums[i] > 0:
                break
            i += 1
        return i+1
            
