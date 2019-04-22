import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # use min heap, push elements on the same column
        # n = len(matrix)
        # m = len(matrix[0])
        # heap = []
        # for j in range(m):
        #     heapq.heappush(heap, (matrix[0][j], 0, j))
        # count = 0
        # while count < k:
        #     (res, i, j)  = heapq.heappop(heap)
        #     if i+1 < n:
        #         heapq.heappush(heap, (matrix[i+1][j], i+1, j))
        #     count += 1
        # return res
        
        # use Binary Search on range
        n = len(matrix)
        m = len(matrix[0])
        lo, hi = matrix[0][0], matrix[n-1][m-1]
        while lo <= hi:
            mid = (lo + hi) / 2
            count = self.countSmall(mid, matrix)
            if count < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo  # existed number and ranks Kth
    
    def countSmall(self, mid, matrix):
        n = len(matrix)
        m = len(matrix[0])
        count = 0
        i = 0
        while i < n:
            j = m-1
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += (j+1)
            i += 1
        return count
        
