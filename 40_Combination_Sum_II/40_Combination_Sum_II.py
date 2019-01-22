class Solution:
    ans = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ## use DFS
        candidates.sort()  # sort first
        self.dfs(candidates, target, 0, [])  # use start index to remove duplicates (since sorted)
        return self.ans
    
    def dfs(self, candidates, target, start, path):
        if target == 0:
            self.ans.append(path[:])  # Note: can use [:] to achieve deep copy
            return
        if start == len(candidates):  # pay attention to i+1
            return
        for i in range(start, len(candidates)):
            num = candidates[i]
            if i > start and num == candidates[i-1]:  # Note: use i > start to remove branch that start with same digits!!
                continue
            if target - num < 0:  # target already smaller than smallest candidates
                break
            path.append(num)
            self.dfs(candidates, target-num, i+1, path)  # use next start to make sure use different digits
            path.pop()
