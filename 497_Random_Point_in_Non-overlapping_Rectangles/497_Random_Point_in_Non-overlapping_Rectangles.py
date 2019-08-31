import random
class Solution:
    ## use area as weight to pick rectangle and then pick random points in the rectangle
    def __init__(self, rects: List[List[int]]):
        self.rects, self.sum = rects, 0
        self.index = []  # index : area accumulation
        for [x1, y1, x2, y2] in rects:
            self.sum += ((x2 - x1 + 1) * (y2 - y1 + 1))  # +1 is for 0-area rectangle
            self.index.append(self.sum)

    def pick(self) -> List[int]:
        area = random.randint(0, self.sum)
        # use binary search for index
        low, high = 0, len(self.index)-1
        while low <= high:
            mid = (low + high) // 2
            if self.index[mid] >= area and (mid == 0 or self.index[mid-1] <= area):
                break
            elif mid > 0 and self.index[mid-1] >= area:
                high = mid-1
            else:
                low = mid+1
        # pick random point in the found rectangle
        [x1, y1, x2, y2] = self.rects[mid]
        x = random.randint(x1, x2)  # could use previous random number to construct point
        y = random.randint(y1, y2)
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
