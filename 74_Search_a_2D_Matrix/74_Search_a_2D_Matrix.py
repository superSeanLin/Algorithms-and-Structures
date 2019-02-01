class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ## bianry search
        ## also can binary search each line
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        r_low, c_low, r_high, c_high = 0, 0, m-1, n-1
        while r_low < r_high or (r_low == r_high and c_low <= c_high):
            r_mid, c_mid = self.findMid(r_low, c_low, r_high, c_high, n)
            if matrix[r_mid][c_mid] > target:
                r_high = r_mid
                c_high = c_mid-1  # edge case?
                if c_high < 0:
                    r_high -= 1
                    if r_high < 0:
                        return False
                    c_high = n-1
            elif matrix[r_mid][c_mid] < target:
                r_low = r_mid
                c_low = c_mid+1
                if c_low >= n:
                    r_low += 1
                    if r_low >= m:
                        return False
                    c_low = 0
            else:
                return True
        return False
    
    def findMid(self, r_low, c_low, r_high, c_high, n):
        rank = ((r_high - r_low) * n + (c_high - c_low) + 1) // 2
        c_mid = c_low + rank
        r_mid = r_low
        if c_low + rank >= n:
            r_mid += 1
            rank -= (n - c_low)
            c_mid = rank % n
        r_mid += rank // n
        return r_mid, c_mid
        
        
