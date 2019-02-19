class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        ## radix sort, but recurse in each bucket
        nums = [str(e) for e in nums]
        length = max(len(num) for num in nums)
        nums = self.radixSort(nums, 0, length)
        return str(int(''.join(nums)))
    
    def radixSort(self, nums, i, length):
        if not nums or i >= length:
            return nums
        bucket = [[] for i in range(10)]
        for e in nums:
            if i >= len(e):
                # digits in the same buckets will have same leading digits, except the end one, thus use that to determine order
                bucket[max(int(e[0]), int(e[-1]))].append(e)  # compare digits in the same bucket
            else:
                bucket[int(e[i])].append(e)
        nums = []
        for each in bucket[::-1]: 
            nums.extend(self.radixSort(each, i+1, length))
        return nums
