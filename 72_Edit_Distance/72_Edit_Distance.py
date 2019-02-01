class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ## classical DP problem
        n = len(word1)
        m = len(word2)
        dis = [[0] * (m+1) for _ in range(n+1)]  # dis(i,j) = minimum distance between word1[i:] and word2[j:], return dis(0,0)
        dis[n][m] = 0
        for i in range(n-1, -1, -1):
            dis[i][m] = n - i
        for j in range(m-1, -1, -1):
            dis[n][j] = m - j
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                minimum = min(dis[i][j+1]+1, dis[i+1][j]+1, dis[i+1][j+1]+1)  # delete j, insert j, replace j
                if word1[i] == word2[j]:
                    dis[i][j] = min(minimum, dis[i+1][j+1])
                else:
                    dis[i][j] = minimum
        return dis[0][0]
