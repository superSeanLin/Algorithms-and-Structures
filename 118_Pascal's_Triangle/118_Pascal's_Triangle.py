class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            prev = ans[i-1]
            row = [0] * (i+1)
            row[0] = 1
            row[-1] = 1
            for idx in range(1, i):
                row[idx] = prev[idx-1] + prev[idx]
            ans.append(row)
        return ans
