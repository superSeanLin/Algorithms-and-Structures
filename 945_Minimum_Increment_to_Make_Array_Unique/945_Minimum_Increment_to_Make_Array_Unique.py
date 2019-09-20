class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # method 1: sort the list and then find what we need for this spot; O(NlogN)
        res, need = 0, 0
        A.sort()
        for x in A:
            res += max(need-x, 0)  # if need < x, reset need to x
            need = max(x+1, need+1)
        return res
        
        # method 2: do same value at one time; O(KlogK) to build heap
        # c = collections.Counter(A)  # value : number
        # res, need = 0, 0
        # for x in sorted(c):
        #     res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) // 2
        #     need = max(need + c[x], x + c[x])
        # return res
        
        # method 3: union find ??
