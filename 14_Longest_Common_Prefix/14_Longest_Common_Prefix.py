class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # vertical scan
        if len(strs) == 0:
            return ""
        s = strs[0]
        i = 0
        for i in range(len(s)):  # for every char, only increase i when all chars meet
            for j in range(1, len(strs)):
                t = strs[j]
                if i >= len(t) or t[i] != s[i]:  # match fail
                    return s[:i]
        return s[:i+1]
