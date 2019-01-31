# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # first find the length of the linked list, and connect tail with head (cycle)
        if not head:
            return head
        n = 1
        p = head
        while p.next:
            n += 1
            p = p.next
        p.next = head
        # then find where to slice
        k = k % n
        p = head
        count = n - k - 1
        while p and count > 0:
            p = p.next
            count -= 1
        # slice
        q = p.next
        p.next = None
        return q
        
        
