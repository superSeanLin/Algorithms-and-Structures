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
        ## recursive method, linked list -> recurse
        ## also naive solution with dict works
        if not head or not head.next:
            return head
        p = head.next
        if p.val != head.val:
            head.next = self.deleteDuplicates(p)
            return head
        else:
            while p and p.val == head.val:
                p = p.next
            return self.deleteDuplicates(p)
