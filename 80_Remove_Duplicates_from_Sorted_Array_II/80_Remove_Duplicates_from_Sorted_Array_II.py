class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:  # no duplicates
            return
        idx, idx2 = 0, 1  # processed indexes, focus on idx (assumed before idx are all perfect)
        for i in range(idx2+1, len(nums)):
            if nums[i] != nums[idx]:  # if idx == idx2, keep both and find new; if idx != idx2, find new 
                idx += 1
                idx2 += 1
                nums[idx2] = nums[i]
        return idx2+1
            
            
