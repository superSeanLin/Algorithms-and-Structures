class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use DP
        length = len(nums)
        if length == 0:
            return 0
        step = [0] * length  # minimum step to last, starting from i
        step[-1] = 0
        for i in range(length-2, -1, -1):
            # if can reach directly, base case
            if nums[i] + i >= length-1:
                step[i] = 1
                continue
            # minimum 2
            minimum = length-1
            j = i + nums[i]
            while j <= length-1 and j >= i+1:  # from buttom to top will much faster than from top to bottom
                temp = 1 + step[j]
                if temp < minimum:
                    minimum = temp
                if minimum == 2:
                    break
                j -= 1
            step[i] = minimum
        return step[0]
        
