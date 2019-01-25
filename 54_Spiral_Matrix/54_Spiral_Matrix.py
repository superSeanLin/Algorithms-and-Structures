class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)  # number of row
        if m == 0:
            return res
        n = len(matrix[0])  # number of col
        if n == 0:
            return res
        layer = (min(m, n)-1) // 2  # layer+1 is the number of layer; at least one layer
        i = 0
        while i <= layer and i < m and i < n:
            #print(matrix[i][i : n-i])
            res += matrix[i][i : n-i]
            #print([a[n-1-i] for a in matrix[i+1 : m-i]])
            res += [a[n-1-i] for a in matrix[i+1 : m-i]]  # get column
            if i != m-1-i:  # already add
                #print(matrix[m-1-i][i : n-1-i][::-1])
                res += matrix[m-1-i][i : n-1-i][::-1]  # reverse
            if i != n-1-i:  # already add
                #print([a[i] for a in matrix[m-2-i : i : -1]])
                res += [a[i] for a in matrix[m-2-i : i : -1]]
            i += 1
        return res
            
