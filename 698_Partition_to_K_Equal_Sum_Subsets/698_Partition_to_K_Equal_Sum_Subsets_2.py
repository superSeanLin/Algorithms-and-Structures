class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # use k-time dfs
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        visited = [False] * len(nums)
        nums = sorted(nums, reverse=True)  # reserve is helpful since we are searching for a working example
        return self.dfs(nums, k, 0, 0, target, visited)
    
    def dfs(self, nums, k, start, curr, target, visited):
        if k == 0:  # 1 partition always true
            return True
        if curr == target:
            return self.dfs(nums, k-1, 0, 0, target, visited)  # if valid, start dfs again until k times
        for i in range(start, len(nums)):
            if not visited[i]:  # not used before
                if curr+nums[i] > target:
                    continue
                visited[i] = True
                if self.dfs(nums, k, i+1, curr+nums[i], target, visited):
                    return True
                visited[i] = False
        return False
