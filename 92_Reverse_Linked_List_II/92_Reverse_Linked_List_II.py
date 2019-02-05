# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    ## can also switch values
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        if m == n or not head or not head.next:
            return head
        superNode = ListNode(0)
        superNode.next = head
        p, q = superNode, head
        start1, start2 = head, head
        count = 0
        while p and q:
            if count+1 == m:
                start1, start2 = p, q
            if count == n:
                break
            if m <= count < n:
                temp = q.next
                q.next = p
                p = q
                q = temp
            else:
                p = q
                q = q.next
            count += 1
        start1.next = p
        start2.next = q
        return superNode.next
