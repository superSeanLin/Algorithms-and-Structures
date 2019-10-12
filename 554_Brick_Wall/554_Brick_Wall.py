class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Basic idea: same as find minimum conflict; could use sorted map
        # improved: since intervals continuous, find number of interval start at this time; then res = len(wall) - num of start
        start_time = {}  # start time : number of interval
        for i in range(len(wall)):
            start = 0
            for num in wall[i][:-1]:  # margin not included
                start += num
                if start not in start_time:
                    start_time[start] = 1
                else:
                    start_time[start] += 1
        return len(wall) - max(start_time.values(), default=0)
