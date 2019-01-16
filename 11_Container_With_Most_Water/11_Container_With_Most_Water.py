class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ## use Dynamic Programming
        if len(height) == 0:
            return 0
        maximum = 0
        i = 0
        j = len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            area = h * (j - i)
            if area > maximum:
                maximum = area
            if height[i] > height[j]:  # area increase only if increase h
                j -= 1
            else:
                i += 1
        return maximum
        
