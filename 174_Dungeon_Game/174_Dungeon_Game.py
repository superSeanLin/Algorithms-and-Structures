class Solution:
    ## start from where princess stayed and with health point 1; DP
    def calculateMinimumHP(self, dungeon: 'List[List[int]]') -> 'int':
        n = len(dungeon)
        m = len(dungeon[0])
        for i in range(n):
            for j in range(m):
                dungeon[i][j] *= -1
        #print(dungeon)
        hp = [[0]*m for i in range(n)]
        hp[n-1][m-1] = 1 + dungeon[n-1][m-1]
        if hp[n-1][m-1] < 1:
            hp[n-1][m-1] = 1
        for i in range(m-2, -1, -1):
            hp[n-1][i] = hp[n-1][i+1] + dungeon[n-1][i]
            if hp[n-1][i] < 1:
                hp[n-1][i] = 1
        for i in range(n-2, -1, -1):
            hp[i][m-1] = hp[i+1][m-1] + dungeon[i][m-1]
            if hp[i][m-1] < 1:
                hp[i][m-1] = 1
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                hp[i][j] = min(hp[i+1][j], hp[i][j+1]) + dungeon[i][j]
                if hp[i][j] < 1:
                    hp[i][j] = 1
        #print(hp)
        return hp[0][0]
