# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        superHead = ListNode(-1)
        superHead.next = head  # parent for head
        p, q = head, superHead  # q is p.previous
        while p and p.val < x:  # star from first greater
            q = p
            p = p.next
        idx = q  # processed pointer
        while p:
            if p.val < x:
                # insert node
                temp = idx.next
                node = ListNode(p.val)
                node.next = temp
                idx.next = node
                idx = idx.next
                # delete node
                q.next = p.next
                p = q.next
            else:
                q = p
                p = p.next
        return superHead.next
                
        
