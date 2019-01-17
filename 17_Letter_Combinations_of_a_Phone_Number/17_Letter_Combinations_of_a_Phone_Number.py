class Solution:
    m = {'1' : ['*'], '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], \
         '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        d = digits[0]
        if len(digits) == 1:
            return self.m[d]
        suffix = self.letterCombinations(digits[1:])
        res = []
        for char in self.m[d]:  # for every possible mapping
            for i in range(len(suffix)):
                res.append(char + suffix[i])
        return res
            
        
