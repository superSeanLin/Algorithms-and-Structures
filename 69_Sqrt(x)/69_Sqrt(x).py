class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ## naive solution is linear search, thus we can optimize with binary search
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2  # also can check the next one
            square = mid * mid
            if square > x:
                high = mid - 1
            elif square < x:
                low = mid + 1
            else:
                return mid
        return high  # low > high
            
