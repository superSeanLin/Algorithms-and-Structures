class Solution:
    # 0-1 knapsack problem; DP with rolling lines
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][x][y] means for 0th~ith string, x 0s, y 1s, the maximum number of formed number
        dp = [[0] * (n+1) for i in range(m+1)]  # base case: dp[0][0] represents 0 0s and 0 1s
        for i in range(len(strs)):
            z = strs[i].count('0')
            o = strs[i].count('1')
            for x in range(m, -1, -1):  # start from m since dp[x-z][y-o] is not updated yet, which represents for dp[i-1][x-z][y-o]
                for y in range(n, -1, -1):
                    if x-z >= 0 and y-o >= 0:
                        dp[x][y] = max(dp[x-z][y-o]+1, dp[x][y])  # include this item or not
        return dp[m][n]
