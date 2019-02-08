class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ## use DP
        if not triangle:
            return 0
        nxtSum = triangle[-1]
        n = len(triangle)
        for i in range(n-2, -1, -1):
            newSum = []
            row = triangle[i]
            m = len(row)
            for j in range(0, m):
                newSum.append(min(row[j] + nxtSum[j], row[j] + nxtSum[j+1]))
            nxtSum = newSum
        return min(nxtSum)
