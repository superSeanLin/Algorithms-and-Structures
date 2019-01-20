class Solution:
    ## may use Euclidean algorithm(辗转相除) to calculate greatest common divisor
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = 1
        if dividend * divisor < 0:  # different sign
            negative = -1
        # make same sigb
        divisor = abs(divisor)
        dividend = abs(dividend)
        quotient = 0
        while dividend >= divisor:
            temp, count = divisor, 1
            while dividend >= temp:  # multiply-like; Note: also for exp
                dividend -= temp
                temp += temp
                quotient += count
                count += count
        return min(max(negative * quotient, -2**31), 2**31-1)
