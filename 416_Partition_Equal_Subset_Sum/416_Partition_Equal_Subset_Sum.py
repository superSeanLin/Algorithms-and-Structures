class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ## 0/1 knapsack problem; classic DP
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        n = len(nums)
        canSum = [[False] * (target+1) for i in range(n)]  # indicates if nums[:i+1] can get sum to j
        for i in range(n):
            canSum[i][0] = True
        for j in range(target+1):
            canSum[0][j] = (j == nums[0])
        for i in range(n):
            for j in range(1, target+1):  # can save time here
                canSum[i][j] = canSum[i-1][j]
                if j - nums[i] >= 0:
                    canSum[i][j] |= canSum[i-1][j-nums[i]]
        return canSum[n-1][target]
