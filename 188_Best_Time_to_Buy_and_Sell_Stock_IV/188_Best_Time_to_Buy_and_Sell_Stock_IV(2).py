class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        ## k-pass DP
        n = len(prices)
        if not n or not k:
            return 0
        if k > n//2:  # Maxprofit II
            maxProfit = 0
            for i in range(n-1):
                if prices[i+1] > prices[i]:
                    maxProfit += prices[i+1] - prices[i]
            return maxProfit
        prevRound = [0] * n  # maximum profit after day i
        buy, sell = prices[-1], prices[-1]
        for i in range(n-1, -1, -1):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > sell:
                buy, sell = prices[i], prices[i]
            diff = sell - buy
            prevRound[i] = diff
            if i < n-1 and prevRound[i] < prevRound[i+1]:
                prevRound[i] = prevRound[i+1]
        for count in range(1, k):
            temp = [0] * n
            buy, sell, prev = prices[-1], prices[-1], 0
            for i in range(n-2, -1, -1):
                if prices[i] < buy:
                    buy = prices[i]
                    temp[i] = sell - buy + prev
                elif prices[i] >= buy:
                    prev_sell, prev_prev = sell, prev
                    buy, sell = prices[i], prices[i]
                    prev = prevRound[i+1]
                    temp[i] = sell - buy + prev
                    if temp[i] < (prev_sell - buy) + prev_prev:
                        temp[i] = (prev_sell - buy) + prev_prev
                        sell = prev_sell
                        prev = prev_prev
                if temp[i] < temp[i+1]:
                    temp[i] = temp[i+1]
            prevRound = temp
        return prevRound[0]
