class Solution:
    def isInterleave(self, s1: 'str', s2: 'str', s3: 'str') -> 'bool':
        ## could use dict to help
        # if not s3:
        #     return not s1 and not s2
        # if not s1:
        #     return s3 == s2
        # elif not s2:
        #     return s3 == s1
        # same = False
        # if s3[0] == s2[0]:
        #     same = same or self.isInterleave(s1, s2[1:], s3[1:])
        # if s3[0] == s1[0]:
        #     same = same or self.isInterleave(s1[1:], s2, s3[1:])
            
        ## use DP to speed up
        l, m, n = len(s1), len(s2), len(s3)
        same = [[[False] * (l+1) for i in range(m+1)] for j in range(n+1)]
        for i in range(m+1):
            for j in range(l+1):
                same[n][i][j] = not s1[i:] and not s2[j:]
        for k in range(n+1):
            for j in range(l+1):
                same[k][m][j] = (s3[k:] == s1[j:])
            for i in range(m+1):
                same[k][i][l] = (s3[k:] == s2[i:])
        for k in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                for j in range(l-1, -1, -1):
                    same[k][i][j] = (s3[k] == s1[j] and same[k+1][i][j+1]) or (s3[k] == s2[i] and same[k+1][i+1][j])       
        return same[0][0][0]
