# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, q = head, head
        if p and p.next:
            q = p.next
            r = q.next  # next head
            q.next = p
            p.next = self.swapPairs(r)
        return q
