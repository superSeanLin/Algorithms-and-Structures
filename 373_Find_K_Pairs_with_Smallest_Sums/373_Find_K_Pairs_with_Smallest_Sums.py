import queue
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int):
        # use heap to find first K
        res = []
        if not nums1 or not nums2 or k == 0:  # empty
            return res
        n = len(nums1)
        m = len(nums2)
        if n * m < k:
            k = n * m
        q = queue.PriorityQueue()
        q.put((nums1[0]+nums2[0], 0, 0))
        count = 0
        while count < k and q.qsize() > 0:
            (currSum, idx1, idx2) = q.get()
            res.append((nums1[idx1], nums2[idx2]))
            count += 1
            if idx2+1 < m:
                q.put((nums1[idx1]+nums2[idx2+1], idx1, idx2+1))
            if idx2 == 0 and idx1+1 < n:  # only increase idx2, avoid duplicates
                q.put((nums1[idx1+1]+nums2[idx2], idx1+1, 0))
        return res
