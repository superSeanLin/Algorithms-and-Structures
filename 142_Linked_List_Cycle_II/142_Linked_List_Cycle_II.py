# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # see if math can deal with this problem
        book = set()
        p = head
        while p:
            if not p in book:
                book.add(p)
            else:
                return p
            p = p.next
        return None
