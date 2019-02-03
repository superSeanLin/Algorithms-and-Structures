# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## traversal; also in-place modify works
        if not head or not head.next:
            return head
        p, q = head, head
        while p:
            q = p
            p = p.next
            while p and p.val == q.val:
                p = p.next
            q.next = p
        return head
