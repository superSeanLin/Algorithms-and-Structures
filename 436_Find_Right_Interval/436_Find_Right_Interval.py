class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index = {}
        for idx, [start, end] in enumerate(intervals):
            index[start] = idx 
        temp = sorted(intervals)  # sorted list
        n = len(intervals)
        res = [0] * n
        for i, interval in enumerate(temp):  # when -1?
            idx = self.binarySearch(temp, i+1, n-1, interval[1])  # index of sorted list
            if idx == -1:
                res[index[interval[0]]] = -1
            else:
                res[index[interval[0]]] = index[temp[idx][0]]
        return res
                
    def binarySearch(self, intervals, low, high, target):
        n = len(intervals)
        while low <= high:
            mid = (low + high) // 2
            if intervals[mid][0] >= target:
                high = mid - 1
            else:
                low = mid + 1
        if high == n-1:  # high didn't move
            if intervals[high][0] >= target:
                return high
            else:  # do not find >=
                return -1
        else:  # the next one is the smallest number >= target
            return high+1
