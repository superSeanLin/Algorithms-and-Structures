class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## may use dict; {sum:[[e1, e2]]}
        ## O(n^2) time complexity, but require distinct numbers
        ans = []
        nums = self.quickSort(nums)  # sort nums first
        # create n list copy, each add an element, still sorted
        n = len(nums)
        res = [[nums[i] + nums[j] for i in range(n) if i != j] for j in range(n)]
        for i in range(len(res)):
            res[i] = self.removeRepeat(res[i])  # until only one
        # use 2Sum; create negative reversed copy and merge, find consecutive same digits
        for i in range(len(res)):
            temp1 = [-x for x in res[i]][::-1]
            temp2 = self.removeRepeat(nums)
            merged = self.merge(temp1, temp2)
            same = self.checkRepeat(merged)
            for e1 in same:
                e2 = nums[i]
                e3 = - e1 - e2
                if e1 != e2 and e2 != e3 and e3 != e1:  # find distinct combination
                    ans.append([e1, e2, e3])
        return ans
    
    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[-1]  # set last element as pivot
        idx, nums = self.partition(nums, pivot)
        left = self.quickSort(nums[:idx])
        right = self.quickSort(nums[idx+1:])
        return left + [pivot] + right
    
    def partition(self, nums, pivot):
        # in-place partition
        idx = 0  # sorted index
        for i in range(len(nums)-1):
            if idx <= i and nums[i] < pivot:  # find a smaller element
                nums[idx], nums[i] = nums[i], nums[idx]  # swap i and idx
                idx += 1
        nums[idx], nums[-1] = nums[-1], nums[idx]  # nums[idx] greater than or equal to pivot
        return idx, nums
    
    def merge(self, l1, l2):
        i, j = 0, 0
        l3 = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                l3.append(l1[i])
                i += 1
            else:
                l3.append(l2[j])
                j += 1
        if i < len(l1):
            l3.extend(l1[i:])
        elif j < len(l2):
            l3.extend(l2[j:])
        return l3
    
    def removeRepeat(self, l1):
        res = []
        helper = set()  # use set to save time
        for x in l1:
            if x not in helper:  # first time meet
                res.append(x)
                helper.add(x)
        return res
    
    def checkRepeat(self, l1):
        same = []
        for i in range(1, len(l1)):
            if l1[i] == l1[i-1]:  # same as previous one
                same.append(l1[i])
        return same
            
