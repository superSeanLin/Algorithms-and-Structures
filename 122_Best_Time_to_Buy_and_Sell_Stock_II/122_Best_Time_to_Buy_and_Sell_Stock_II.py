class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## find the maximum difference, from bottom to top
        sell = 0
        buy = 0  # keep buy <= sell
        maximum = 0
        n = len(prices)
        for i in range(n-1, -1, -1):
            if prices[i] > sell:
                sell = prices[i]
                buy = sell
            if prices[i] < buy:
                buy = prices[i]
            diff = sell - buy
            if diff > maximum:
                maximum = diff
        return maximum
