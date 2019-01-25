class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for i in range(n)]
        layer_num = n // 2
        start = 1
        layer = 0
        while layer <= layer_num:
            if layer == n-1-layer:
                res[layer][layer] = start  # single core
            for j in range(layer, n-1-layer):
                res[layer][j] = start
                start += 1
            for i in range(layer, n-1-layer):
                res[i][n-1-layer] = start
                start += 1
            for j in range(n-1-layer, layer, -1):
                res[n-1-layer][j] = start
                start += 1
            for i in range(n-1-layer, layer, -1):
                res[i][layer] = start
                start += 1
            layer += 1
        return res
