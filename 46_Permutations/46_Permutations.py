class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # sort first
        original = nums[:]
        res = []
        res.append(nums[:])
        while True:
            self.nextPermute(nums)
            #print(nums, original)
            if nums == original:
                break
            res.append(nums[:])
        return res
    
    def nextPermute(self, nums):
        # find leading number
        i = len(nums)-1
        while i >= 1:
            if nums[i-1] < nums[i]:  # nums[i-1] is the leading number
                break
            i -= 1
        if i == 0:  # last permutation
            nums.reverse()
            return
        minimum = 2**31-1
        idx = i  # number to be swap
        for j in range(i, len(nums)):
            if nums[j] < minimum and nums[j] > nums[i-1]:
                minimum = nums[j]
                idx = j
        nums[i-1], nums[idx] = nums[idx], nums[i-1]
        # reverse nums[i:]
        j = len(nums)-1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return
