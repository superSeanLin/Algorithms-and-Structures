import re
class Solution:
    def calculate(self, s: str) -> int:
        # no parentheses; build postfix expression and use stack
        s = self.buildPost(re.split('(\W)', s))
        stack = []
        for e in s:
            if e.isdigit():
                stack.append(int(e))
            elif e == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif e == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif e == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif e == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(a//b)
        return stack[0]
        
    def buildPost(self, s):
        res = []
        stack = [(None, -1)]  # (operator, priority); -,+ -> 0; *,/ -> 1
        pri = {'-': 0, '+': 0, '*': 1, '/': 1}
        for e in s:
            if e.isdigit():
                res.append(e)
            elif e in pri:
                while stack[-1][1] >= pri[e]:  # make sure all lower priority operator remaining
                    res.append(stack.pop()[0])
                stack.append((e, pri[e]))
        while stack[-1][0] != None:
            res.append(stack.pop()[0])
        return res
