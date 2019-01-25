# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ## naive solution, maybe use recurse
        # first sort the list
        intervals = sorted(intervals, key = lambda inter:inter.start)
        n = len(intervals)
        res = []
        i = 0
        while i < n:
            start1 = intervals[i].start
            end1 = intervals[i].end  # maximum end
            for j in range(i, n):
                start2 = intervals[j].start
                if start2 > end1:
                    res.append([start1, end1])
                    i = j-1
                    break
                end2 = intervals[j].end
                end1 = max(end1, end2)
                if j == n-1:  # last one
                    end2 = intervals[j].end
                    res.append([start1, end1])
                    i = j
            i += 1
        return res
