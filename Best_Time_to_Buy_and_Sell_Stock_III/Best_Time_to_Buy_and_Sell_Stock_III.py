class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## two pass, DP, first pass find the maximum single transaction; o(n)
        ## also can use recursive method
        if not prices:
            return 0
        n = len(prices)
        single = [0] * n  # maximum single transaction after i
        buy, sell = prices[-1], prices[-1]
        for i in range(n-1, -1, -1):  # O(n)
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] > sell:
                buy, sell = prices[i], prices[i]
            diff = sell - buy
            single[i] = diff
            if i < n-1 and single[i] < single[i+1]:
                single[i] = single[i+1]
        double = [0] * n
        buy, sell = prices[-1], prices[-1]
        second = 0
        for i in range(n-2, -1, -1):
            print(i, prices[i], buy, sell, second)
            if prices[i] < buy:
                buy = prices[i]
                double[i] = sell - buy + second
            elif prices[i] >= buy:  # Guess: maybe the greatest two?
                prev_sell, prev_second = sell, second
                buy, sell = prices[i], prices[i]
                second = single[i+1]
                double[i] = sell - buy + second
                if double[i] < (prev_sell - buy) + prev_second:
                    double[i] = (prev_sell - buy) + prev_second
                    sell = prev_sell
                    second = prev_second
            if double[i] < double[i+1]:
                double[i] = double[i+1]
        return double[0] 
