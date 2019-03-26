import queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## use heap, keep k elements in heap
        res = []
        if k == 0 or not nums:
            return res
        q = queue.PriorityQueue()
        for i in range(k-1):  # initial heap
            q.put((-1*nums[i], i))  # max heap
        for end in range(k-1, len(nums)):
            q.put((-1*nums[end], end))
            while True:  # until within the valid range
                (val, idx) = q.get()
                if idx > end-k:
                    res.append(-1*val)
                    q.put((val, idx))  # put back
                    break
        return res
