class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        res = [[]]
        nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            j = i+1
            while j < n and nums[i] == nums[j]:
                j += 1
            temp = self.subsetsWithDup(nums[j:])
            for k in range(i, j):
                for t in temp:
                    res.append(nums[i:k+1]+t)
            i = j
        return res
