class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ## use Recursive method; start can represent any char
        if not s and not p:
            return True
        if (s and s[0] != "*" and not p) or (p and p[0]!= "*" and not s):
            return False
        # start with *
        if (s and s[0] == "*") or (p and p[0] == "*"):
            if s and s[0] == "*":
                return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
            elif p and p[0] == "*":
                return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        # not start with *
        else:
            if s[0] == p[0] or s[0] == "." or p[0] == ".":
                return self.isMatch(s[1:], p[1:])
           
            
