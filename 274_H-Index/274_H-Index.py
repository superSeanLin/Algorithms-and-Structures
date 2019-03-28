class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ## find a kth number that greater than or equal to k
        ## sorting and binary search
        # n = len(citations)
        # if n == 0:
        #     return 0
        # citations = sorted(citations, reverse=True)  # max -> min
        # low, high = 0, n-1
        # maximum = 0
        # while low <= high:
        #     mid = (low+high) // 2
        #     if citations[mid] >= mid+1:
        #         maximum = max(mid+1, maximum)
        #         low = mid + 1
        #     elif citations[mid] < mid+1:
        #         high = mid - 1
        # return maximum
        
        ## consider quick select
        return self.quickSelect(citations, 0, len(citations)-1)
    
    def quickSelect(self, citations, start, end):
        if end < start:
            return 0
        idx = self.partition(citations, start, end)
        if citations[idx] >= idx+1:
            return max(self.quickSelect(citations, idx+1, end), idx+1)
        else:
            return self.quickSelect(citations, start, idx-1)
        
    def partition(self, citations, start, end):
        pivot = citations[end]
        idx = start  # processed index
        for i in range(start, end):
            if citations[i] >= pivot:
                citations[i], citations[idx] = citations[idx], citations[i]
                idx += 1
        citations[idx], citations[end] = citations[end], citations[idx]
        return idx
