import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        ## use maxHeap for lower half and minHeap for upper half
        self.maxHeap = []  # should use negative to achieve
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0:  # initialization
            heapq.heappush(self.maxHeap, -1*num)
        else:
            if num > -1*self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -1*num)
        if len(self.maxHeap) > len(self.minHeap)+1:  # keep len(max) <= len(min)+1
            item = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1*item)
        elif len(self.minHeap) > len(self.maxHeap):
            item = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*item)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):  # even length
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:  # odd length
            return -1.0 * self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
