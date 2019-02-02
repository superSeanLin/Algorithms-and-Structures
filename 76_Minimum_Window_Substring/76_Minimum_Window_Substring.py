class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ## sliding window
        dic = {}  # store needed char
        index = {}  # store char index, stack
        for char in t:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
                index[char] = []
        count = 0  # met char
        n = len(t)
        first = 0  # first index of the current window
        start = 0  # start index of the shortest window
        length = len(s)
        for i, char in enumerate(s):
            if char in dic:
                index[char].append(i)
                if dic[char] > 0:
                    dic[char] -= 1
                    count += 1
                else:
                    index[char].pop(0)
            if count == n:
                first = self.getFirst(index, s)  # each char must have a valid list
                temp = i - first + 1
                if temp < length:
                    start = first
                    length = temp
        if count == n:
            return s[start:start+length]
        else:
            return ""
        
    def getFirst(self, index, s):
        minimum = len(s)-1
        for char in index:
            if index[char][0] < minimum:
                minimum = index[char][0]
        return minimum
