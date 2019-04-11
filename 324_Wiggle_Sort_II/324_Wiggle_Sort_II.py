class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## first find median, then distribute digits > median, == median and < median on even and odd indecies; 
        ## see discussion for further idea
        # global ordering is unnecessary, very naive method
        n = len(nums)
        for i in range(n):
            nums[0], nums[i] = nums[i], nums[0]  # start with every possibility
            if self.helper(nums, 0):
                break
            nums[0], nums[i] = nums[i], nums[0]
    
    def helper(self, nums, idx):
        n = len(nums)
        if idx == n-1:
            return True
        if idx % 2 == 0:  # even index, need greater
            for i in range(idx+1, n):
                if nums[i] > nums[idx]:
                    nums[i], nums[idx+1] = nums[idx+1], nums[i]
                    if self.helper(nums, idx+1):
                        return True
                    nums[i], nums[idx+1] = nums[idx+1], nums[i]  # compensate effect
        else:  # odd index, need smaller
            for i in range(idx+1, n):
                if nums[i] < nums[idx]:
                    nums[i], nums[idx+1] = nums[idx+1], nums[i]
                    if self.helper(nums, idx+1):
                        return True
                    nums[i], nums[idx+1] = nums[idx+1], nums[i]  # compensate effect
        return False
                
