# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        superNode = ListNode(-1)
        superNode.next = l1
        p, q, r = superNode, l1, l2  # p = q.prev
        while q and r:
            if q.val >= r.val:
                temp = r.next
                p.next = r
                p = r
                r.next = q
                r = temp
            else:
                p = q
                q = q.next
        if r:
            p.next = r
        return superNode.next
