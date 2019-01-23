class Solution:
    def rotate(self, nums):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(nums)
        layer = n // 2  # layer+1 = # of layer
        while layer >= 0:
            for i in range(layer, n-layer-1):
                nums[layer][i], nums[i][n-1-layer], nums[n-1-layer][n-1-i], nums[n-1-i][layer] = \
                nums[n-1-i][layer], nums[layer][i], nums[i][n-1-layer], nums[n-1-layer][n-1-i]
            layer -= 1
