class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ## DP, O(n^3); consider which is the last burst balloon since already burst balloon won't affect
        n = len(nums)
        nums = [1] + nums + [1]  # make it convenient
        if n == 0:
            return 0
        coins = [[0] * (n+2) for i in range(n+2)]  # indicates max Coins from i to j
        for diff in range(1, n+1):  # length of [i,j]
            for i in range(1, n+2-diff):
                j = i + diff - 1
                for k in range(i, j+1):
                    # we need max before k, after k and coins finally bursting k
                    # k can be any from i to j; k before and after all burst, need i-1, j+1
                    coins[i][j] = max(coins[i][j], coins[i][k-1] + coins[k+1][j] + nums[i-1]*nums[k]*nums[j+1])
        return coins[1][n]
