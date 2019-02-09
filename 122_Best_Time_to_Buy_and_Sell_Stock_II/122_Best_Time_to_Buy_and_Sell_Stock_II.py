class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy, sell = prices[0], prices[0]
        sum = 0
        for i in range(1, len(prices)):
            if prices[i] > sell:
                sell = prices[i]
            if prices[i] < sell or i == len(prices)-1:  # already sell or last one    
                diff = sell - buy
                sum += diff
                buy, sell = prices[i], prices[i]
        return sum
                
