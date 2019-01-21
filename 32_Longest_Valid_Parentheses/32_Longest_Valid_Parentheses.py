class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## use Stack
        stack = [-1]  # stack of index; initialize with -1
        maximum = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:  # ')'
                stack.pop()  # if stack[-1] == '(', pop and get right length; if stack[-1] == ')', pop it and get length 0
                if len(stack) == 0:  # empty stack
                    stack.append(i)
                else:
                    maximum = max(maximum, i - stack[-1])
        return maximum
