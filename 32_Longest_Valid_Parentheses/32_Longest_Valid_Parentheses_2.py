class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # use left/right counter
        left, right = 0, 0
        n = len(s)
        maxi = 0
        for i in range(n):  # from left to right
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxi = max(maxi, left*2)
            if right > left:  # not valid anymore; similar as first method, however we cannot calculate "((())" case, so need traverse from the other end
                left, right = 0, 0
        left, right = 0, 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxi = max(maxi, left*2)
            if left > right:
                left, right = 0, 0
        return maxi
