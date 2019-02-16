# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points: 'List[Point]') -> 'int':
    ## use dict, gcd, hash code / cantor pairing
        n = len(points)
        if not n :
            return 0
        if n == 1:
            return 1
        line = {}  # slope : count, for each point, count how many other points on the same line
        maxPoint = 0
        for i in range(n):
            line.clear()
            localMax = 0
            same = 1
            for j in range(i+1, n):
                x1, y1, x2, y2 = points[i].x, points[i].y, points[j].x, points[j].y
                dx = x2 - x1
                dy = y2 - y1
                sign = 1
                if dx * dy < 0:
                    sign = -1
                    dx = abs(dx)
                    dy = abs(dy)  # cantor pairing only deals with non-negative integer
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                dev = self.gcd(dx, dy)  # gcd to avoid float
                if dev != 0:
                    dx /= dev
                    dy /= dev
                m = sign*(dx + dy)*(dx + dy + 1) // 2 + dy  # cantor pair create unique hashcode for each slope
                if m in line:
                    line[m] += 1
                else:
                    line[m] = 1
                localMax = max(localMax, line[m])
            maxPoint = max(maxPoint, localMax+same)
        return maxPoint

    def gcd(self, x, y):
        while y:
            z = x % y
            x = y
            y = z
        return x
            
