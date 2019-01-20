class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # All words are the same length
        res = []
        if not words:  # no valid words
            return res
        length_text = len(s)
        num = len(words)
        length_word = len(words[0])
        counter = {}
        for w in words:
            if not w in counter:
                counter[w] = 1
            else:  # old words
                counter[w] += 1
        for i in range(length_text - num*length_word + 1):  # valid length
            temp = counter.copy()
            n = num
            for j in range(num):
                w = s[i + j*length_word : i + (j+1)*length_word]
                if w in temp:  # valid words
                    temp[w] -= 1
                    if temp[w] < 0:
                        n < 0
                        break
                    n -= 1
            if n == 0:
                res.append(i)
        return res
                
