class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ## use Dynamic Programming
        cs = [set() for i in range(target)]  # use set to keep unique tuples
        if 1 in candidates:
            cs[0].add((1,))
        for i in range(2, target+1):
            comb = self.extract(i)
            for c in comb:
                x, y = c[0]-1, c[1]-1
                for comb1 in cs[x]:
                    for comb2 in cs[y]:
                        cs[i-1].add(tuple(sorted(list(comb1 + comb2))))
            if i in candidates:  # self include
                cs[i-1].add((i,))
        return list(cs[target-1])
    
    def extract(self, target):
        comb = []
        for i in range(1, target//2 + 1):
            comb.append((i, target-i))
        return comb
        
