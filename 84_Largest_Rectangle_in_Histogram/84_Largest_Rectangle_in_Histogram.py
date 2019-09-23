class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ## BFS, same idea as path sum; O(nlogn)
        if not heights:
            return 0
        i, j = 0, len(heights)-1
        mid = (i + j) // 2
        left = self.largestRectangleArea(heights[:mid])
        right = self.largestRectangleArea(heights[mid+1:])
        included = 0  # largest area included mid
        while i <= j and i <= mid and j >= mid:  # idea from No.11
            h = min(heights[i:j+1])
            w = j - i + 1
            temp = h * w
            if temp > included:
                included = temp
            min_left = min(heights[i:mid+1])
            min_right = min(heights[mid:j+1])
            if min_left < min_right:
                i += heights[i:mid+1].index(min_left)
                i += 1
            else:
                j = mid + heights[mid:j+1].index(min_right)
                j -= 1
        return max(included, left, right)
        
            
