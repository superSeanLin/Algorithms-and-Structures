class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## use quickSelect; can also use heap
        res = []
        if not nums:
            return res
        book = {}  # num : counter
        for e in nums:
            if not e in book:
                book[e] = 1
            else:
                book[e] += 1
        # conver to a list
        for num in book:
            res.append((book[num], num))
        res = self.quickSelect(res, k)
        return res
    
    def quickSelect(self, nums, k):
        idx = self.partition(nums)
        if idx+1 == k:
            return [x[1] for x in nums[:idx+1]]
        elif idx+1 < k:
            return [x[1] for x in nums[:idx+1]] + self.quickSelect(nums[idx+1:], k-idx-1)
        else:  # idx+1 > k
            return self.quickSelect(nums[:idx], k)
        
    def partition(self, nums):
        pivot = nums[-1][0]  # counte comparison
        idx = 0  # processed index
        for i in range(len(nums)-1):
            if nums[i][0] > pivot:  # bigger left
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[-1] = nums[-1], nums[idx]
        return idx
