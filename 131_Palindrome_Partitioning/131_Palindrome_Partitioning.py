class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        res = []
        if not s:
            return [[]]
        #res.append(list(set(s)))  # all single
        n = len(s)
        for i in range(n):
            if s[:i+1] == s[:i+1][::-1]:  # palindrom
                temp = [s[:i+1]]
                remain = self.partition(s[i+1:])
                for r in remain:
                    res.append(temp + r)
        return res
        
