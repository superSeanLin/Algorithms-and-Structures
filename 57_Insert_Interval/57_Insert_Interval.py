# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        start2 = newInterval.start  # merged interval start
        end2 = newInterval.end  # merged interval end
        n = len(intervals)
        if n == 0:
            return [[start2, end2]]
        merged = False
        for i in range(n):
            inter = intervals[i]
            start1 = inter.start
            end1 = inter.end
            if merged:
                res.append([start1, end1])
            else:  # new interval exist
                if end2 < start1:  # previous interval
                    res.append([start2, end2])
                    res.append([start1, end1])
                    merged = True
                elif start2 > end1:  # next interval
                    res.append([start1, end1])
                    if i == n-1:
                        res.append([start2, end2])
                elif start2 >= start1 and end2 <= end1:  # included interval
                    res.append([start1, end1])
                    merged = True
                elif start2 <= start1 and end2 <= end1:
                    end2 = end1
                    if i == n-1:
                        res.append([start2, end2])
                elif start2 >= start1 and end2 >= end1:
                    start2 = start1
                    if i == n-1:
                        res.append([start2, end2])
                else:  #start2 <= start1 and end2 >= end1
                    if i == n-1:
                        res.append([start2, end2])
        return res
        
