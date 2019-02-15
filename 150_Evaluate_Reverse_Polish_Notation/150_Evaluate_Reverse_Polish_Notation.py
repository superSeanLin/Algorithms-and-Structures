class Solution:
    def evalRPN(self, tokens: 'List[str]') -> 'int':
        stack = []
        for e in tokens:
            if e in ('+', '-', '*', '/'):
                a = stack.pop()
                b = stack.pop()
                c = 0
                if e == '+':
                    c = a + b
                elif e == '-':
                    c = b - a
                elif e == '*':
                    c = a * b
                else:
                    c = int(b / a)
                stack.append(c)
            else:
                stack.append(int(e))
        return stack[0]
