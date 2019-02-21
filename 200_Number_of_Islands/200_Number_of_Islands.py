class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
    ## use a dict; or withou a dict, use DFS to mark all connected land other digit
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0
        land = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not (i, j) in land:
                    count += 1
                    self.DFS(i, j, grid, land)
        return count
    
    def DFS(self, i, j, grid, land):
        m = len(grid)
        n = len(grid[0])
        land.add((i, j))
        if i > 0 and grid[i-1][j] == "1" and not (i-1, j) in land:
            self.DFS(i-1, j, grid, land)
        if i < m-1 and grid[i+1][j] == "1" and not (i+1, j) in land:
            self.DFS(i+1, j, grid, land)
        if j > 0 and grid[i][j-1] == "1" and not (i, j-1) in land:
            self.DFS(i, j-1, grid, land)
        if j < n-1 and grid[i][j+1] == "1" and not (i, j+1) in land:
            self.DFS(i, j+1, grid, land)
