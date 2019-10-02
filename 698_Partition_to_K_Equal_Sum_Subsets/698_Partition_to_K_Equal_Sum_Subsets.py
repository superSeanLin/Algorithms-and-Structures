class Solution:
    def __init__(self):
        self.ans = False
        
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # use dfs; very slow
        nums.sort()
        target = sum(nums) // k
        if target * k != sum(nums):
            return False
        t = [target] * k  # for each partation
        self.dfs(nums, t)
        return self.ans
    
    def dfs(self, nums, t):  # basic idea is each element can be placed in each partition
        if sum(t) == 0:  # all used
            self.ans = True
            return
        curr = nums.pop()
        for j in range(len(t)):
            if t[j] < curr:
                continue  # problem here
            t[j] -= curr
            self.dfs(nums, t)
            t[j] += curr
        nums.append(curr)
