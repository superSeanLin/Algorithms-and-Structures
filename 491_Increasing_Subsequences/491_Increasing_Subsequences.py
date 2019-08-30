class Solution:
    # typical DFS with no duplication; Basic idea is not to use same element in the same layer
    def __init__(self):
        self.ans = []
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, start, temp):
            if len(temp) >= 2:
                self.ans.append(temp[:])
            if start == len(nums):
                return
            layerUsed = set()  # avoid use same element on the same layer; new layers will allocate new sets
            for i in range(start, len(nums)):
                if (not temp or nums[i] >= temp[-1]) and (nums[i] not in layerUsed):
                    layerUsed.add(nums[i])
                    temp.append(nums[i])
                    dfs(nums, i+1, temp)
                    temp.pop(-1)
        dfs(nums, 0, [])
        return self.ans
