import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # reservoir sampling; start with k reservoirs; for k+i, pick it with k/k+i possibility and then replace a reservoir randomly;
    # number stay in reservoir with possibility k/k+i-1 * (1 - k/k+i * 1/k) = 1/k+i
    # ideas see discussion
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        k, p = self.head.val, self.head.next
        n = 1
        while p:
            if random.randint(1, n+1) == n:
                k = p.val
            p = p.next
            n += 1
        return k


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
