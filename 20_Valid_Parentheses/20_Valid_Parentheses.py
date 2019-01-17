class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## use Stack to deal with parenthese
        if len(s) % 2 != 0:  # odd number
            return False
        stack = []  # use list as stack
        left = ['(', '[', '{']
        right = {')' : '(', ']' : '[', '}' : '{'}
        for i in range(len(s)):
            if s[i] in right:  # right parenthese
                if len(stack) > 0 and stack[-1] == right[s[i]]:
                    stack.pop()  # remove corresponding left parenthese
                else:  # cannot match
                    return False
            else:  # left parenthese
                stack.append(s[i])
        return (len(stack) == 0)  # if only right parenthese
