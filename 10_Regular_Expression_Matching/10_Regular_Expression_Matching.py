class Solution:
  ## can use DP to save time
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:  # no pattern
            return not s
        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')  # string valid and first match
        if len(p) >= 2 and p[1] == '*':  # '*' must show up at p[1]
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))  # '*' Matches zero or more of the preceding element
        else:  # no '*' situation
            return first_match and self.isMatch(s[1:], p[1:])
