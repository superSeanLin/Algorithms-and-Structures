class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## DP, O(n)
        n = len(prices)
        if n == 0:
            return 0
        hold = [0] * n  # indicates maxProf if we hold a stock at ith day
        unhold = [0] * n
        cool = [0] * n
        hold[0] = -1*prices[0]
        for i in range(1, n):
            # if plan to hold: 1. already hold; 2. buy after cooldown
            hold[i] = max(hold[i-1], cool[i-1]-prices[i])
            # if plan to unhold: 1. already unhold; 2. sell hold
            unhold[i] = max(unhold[i-1], hold[i-1]+prices[i])
            # if plan to cooldown: 1. sell yesterday 2. do nothing yesterday
            cool[i] = max(cool[i-1], unhold[i-1])
        return unhold[n-1]  # last sell
        
        
        ## DP, O(n^2)
        # n = len(prices)
        # if n <= 1:
        #     return 0
        # prof = [0] * (n+2)  # indicates maxProf starting from i; also could use maxPorf buying at index i
        # if prices[-2] < prices[-1]:
        #     prof[n-2] = (prices[-1] - prices[-2])
        # for i in range(n-3, -1, -1):
        #     maxi = 0
        #     for j in range(i+1, n):  # buy at index i
        #         if prices[j] > prices[i]:
        #             maxi = max(maxi, prices[j]-prices[i]+prof[j+2])  # j+2 always valid and prof[j-1~j+1] = 0 
        #     prof[i] = max(prof[i+1], maxi)  # not buy at index i
        # return prof[0]
            
        
