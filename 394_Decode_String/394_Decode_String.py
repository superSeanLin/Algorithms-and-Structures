class Solution:
    def decodeString(self, s: str) -> str:
        book = self.getIndex(s)  # index of "[" : index of corresponding "]"
        res = self.helper(s, book)
        return res
    
    def helper(self, s, book):
        res = ""
        if not s:
            return res
        n = len(s)
        i = 0
        rep = 0
        while i < n:
            if s[i].isdigit():
                rep = rep * 10 + int(s[i])
            else:
                if s[i] == '[':
                    j = book[i]
                    res += self.decodeString(s[i+1:j]) * rep
                    i = j
                elif s[i].isalpha():
                    res += s[i]
                rep = 0
            i += 1
        return res
    
    def getIndex(self, s):
        book = {}
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == "[":
                stack.append(i)
            elif s[i] == ']':
                j = stack.pop()
                book[j] = i  # "[" : "]"
        return book
                
