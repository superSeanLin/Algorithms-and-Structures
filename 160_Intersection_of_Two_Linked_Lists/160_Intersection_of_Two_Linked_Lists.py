# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ## also use length to decide start pointer, then keep moving until pointers meet
        book = set()
        p = headA
        while p:
            book.add(p)
            p = p.next
        p = headB
        while p:
            if p in book:
                return p
            p = p.next
        return None
