class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ## MergeSort-based solution is a standard way to solve problems related to inverse numbers
        ## Note: elements of b come after elements of a; O(nlogn)
        if not nums:
            return []
        res, index = self.mergeSort(nums, list(range(len(nums))))
        ans = [0] * len(nums)
        for count, i in enumerate(index):
            ans[i] = res[count][1]
        return ans
    
    def mergeSort(self, nums, index):  # if space sufficient, we can do in-place; see #88
        n = len(nums)
        if n == 1:  # base case
            return [(nums[0], 0)], index
        a, indexA = self.mergeSort(nums[:n//2], index[:n//2])
        b, indexB = self.mergeSort(nums[n//2:], index[n//2:])
        merged = 0  # indicates number of merged elements from b
        i, j = 0, 0
        res = []  # (element, number smaller after)
        new_index = []
        while i < len(a) and j < len(b):
            if a[i][0] <= b[j][0]:  # use <= to avoid increasing merged when equal
                res.append((a[i][0], a[i][1]+merged))
                new_index.append(indexA[i])
                i += 1
            else:
                merged += 1
                res.append((b[j][0], b[j][1]))
                new_index.append(indexB[j])
                j += 1
        if i < len(a):
            res.extend([(x[0], x[1]+merged) for x in a[i:]])
            new_index.extend(indexA[i:])
        if j < len(b):
            res.extend(b[j:])
            new_index.extend(indexB[j:])
        return res, new_index
