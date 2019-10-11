# 253: meeting room II

# method 1: use heap
from heapq import *

def findNumber(meeting):
	# for each start, find number of end overlapping
	meeting.sort(key = lambda x : (x[0], x[1]))
	end = [meeting[0][1]]
	maxi = 1
	for i in range(1, len(meeting)):
		start, end_next = meeting[i][0], meeting[i][1]
		while end and end[0] < start:  # not overlapped
			heappop(end)
		heappush(end, end_next)
		maxi = max(maxi, len(end))
	return maxi

# method 2: use sorted map; map[start] -> +1, map[end] -> -1, finally traverse the sorted map
