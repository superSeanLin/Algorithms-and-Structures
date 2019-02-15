# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head
        q = head.next  # q to be inserted
        head.next = None
        while q:
            temp = q.next
            q.next = None
            head = self.insert(head, q)
            q = temp
        return head
    
    def insert(self, head, node):
        superNode = ListNode(min(head.val, node.val)-1)
        superNode.next = head
        p, q = superNode, superNode  # p is prev of q
        while q and node.val > q.val:
            p = q
            q = q.next
        p.next = node
        node.next = q
        return superNode.next
        
        
