import re
class Solution:
    def calculate(self, s: str) -> int:
        ## first build post-order expression, then use stack to calculate
        s = self.buildPost(re.split('(\W)', s))  # [^a-zA-Z0-9_], (\W) keeps separators
        stack = []  # only contain digits and "("
        for e in s:
            if e.isdigit():
                stack.append(int(e))
            elif e == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif e == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
        return stack[0]
        
    def buildPost(self, s):
        ## in the post-order expression, rightmost has lowest priority
        res = []  # output 
        stack = [(None, -1)]  # (operator, priority)
        p = 0
        for e in s:
            if e.isdigit():
                res.append(e)
            elif e == '-' or e == "+":
                while stack[-1][1] >= p:  # make sure all operators in stack with prioirty < current priority
                    res.append(stack.pop()[0])
                stack.append((e, p))
            elif e == '(':
                stack.append((e, p))
                p += 1
            elif e == ')':  # find last '('
                while stack[-1][0] != '(':
                    res.append(stack.pop()[0])
                stack.pop()
                p -= 1
        while stack[-1][0] != None:
            res.append(stack.pop()[0])
        return res
                    
