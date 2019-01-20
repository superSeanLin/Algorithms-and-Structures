class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ## Working solution with KMP but need high demand of memory and time
        res = []
        if len(words) == 0:
            return res
        substrings = self.concateWords(words)
        #print(substrings)
        for sub in substrings:
            pi = self.createPI(sub)
            idx = -1
            for i in range(len(s)):
                while idx > -1 and s[i] != sub[idx+1]:
                    idx = pi[idx]
                if s[i] == sub[idx+1]:
                    idx += 1
                if idx == len(sub)-1:
                    res.append(i - len(sub) + 1)
                    idx = pi[idx]  # look for next
        return res     
        
    def createPI(self, words):
        pi = [-1]
        idx = -1
        for i in range(1, len(words)):
            while idx > -1 and words[idx+1] != words[i]:
                idx = pi[idx]
            if words[idx+1] == words[i]:
                idx += 1
            pi.append(idx)
        return pi
    
    def concateWords(self, words):
        if len(words) == 1:
            return words
        res = set()
        for i in range(len(words)):
            temp = words.copy()
            temp.remove(words[i])
            res_next = self.concateWords(temp)
            for s in res_next:
                res.add(s + words[i])
        return res
            
    
