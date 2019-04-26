class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # devide and conquer
        for c in set(s):
            if s.count(c) < k:  # for first rare character
                return max(self.longestSubstring(t, k) for t in s.split(c))  # never include that char
        return len(s)
