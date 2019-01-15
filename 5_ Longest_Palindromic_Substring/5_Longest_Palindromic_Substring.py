class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## use Dynamic Programming, also can apply to longest subsequence
        length = len(s)
        count = [[0] * length for i in range(length)]  # (i, j); length of palindromic substring start from i, ending j
        maximum = 1
        index = (length-1, length-1)
        for i in range(length):
            count[i][i] = 1
            if i < length-1 and s[i] == s[i+1]:
                count[i][i+1] = 2
        for i in range(length-1, -1, -1):
            for j in range(i+1, length):
                if (s[i] == s[j] and count[i+1][j-1]):
                    count[i][j] = count[i+1][j-1] + 2
                else:
                    count[i][j] = max(count[i][j], 0)
                if count[i][j] >= maximum:
                    maximum = count[i][j]
                    index = (i, j)
        return s[index[0] : index[1]+1]
