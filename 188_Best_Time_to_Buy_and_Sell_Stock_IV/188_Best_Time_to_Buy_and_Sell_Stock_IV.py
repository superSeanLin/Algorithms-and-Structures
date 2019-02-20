class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        ## k-pass DP; with help of hold and unhold
        n = len(prices)
        if not n:
            return 0
        if k > n//2:  # Maxprofit II
            maxProfit = 0
            for i in range(n-1):
                if prices[i+1] > prices[i]:
                    maxProfit += prices[i+1] - prices[i]
            return maxProfit
        dphold = [[0] * (k+1) for i in range(n)]  # max profit in day i, having j transactions, holding a stock
        dpunhold = [[0] * (k+1) for i in range(n)]
        # base case 1: day 1 hold one stock 
        for j in range(k):
            dphold[0][j] = -prices[0]
        # base case 2: 0 transaction; buy the cheapest so far
        for i in range(1, n):
            dphold[i][0] = max(dphold[i-1][0], -prices[i])
        for j in range(1, k+1):
            for i in range(1, n):
                # if plan to hold: 1. you already have one; 2. no holding
                dphold[i][j] = max(dphold[i-1][j], dpunhold[i-1][j]-prices[i])
                # if plan to release: 1. you already have one; 2. no holding
                dpunhold[i][j] = max(dphold[i-1][j-1]+prices[i], dpunhold[i-1][j])
        return max(dpunhold[n-1][k], dphold[n-1][k])
