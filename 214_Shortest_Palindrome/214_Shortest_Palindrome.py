class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # start from the middle to find the anchor; only insert in front of it
        ## idea of using KMP to find the longest prefix of reverse is very brilliant!!!
        n = len(s)
        if n <= 1:
            return s
        for i in range(n-1, -1, -1):
            if s[:i+1] == s[:i+1][::-1]:  # palindrome
                break
        return s[i+1:][::-1] + s
