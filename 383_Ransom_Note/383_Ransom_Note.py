class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = {}
        for char in magazine:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1
        for char in ransomNote:
            if not char in m or m[char] <= 0:
                return False
            else:
                m[char] -= 1
        return True
        
