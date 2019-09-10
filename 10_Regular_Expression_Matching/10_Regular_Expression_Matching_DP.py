class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ## used Recursive method; DP method
        match = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        match[-1][-1] = True  # both empty
        for i in range(len(s), -1, -1):  # special cases: "" and "a*"
            for j in range(len(p)-1, -1, -1):
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                if j+1 < len(p) and p[j+1] == '*':  # entries for p[j] == '*' are useless
                    match[i][j] = match[i][j+2] or (first_match and match[i+1][j])
                else:
                    match[i][j] = first_match and match[i+1][j+1]
        return match[0][0]
