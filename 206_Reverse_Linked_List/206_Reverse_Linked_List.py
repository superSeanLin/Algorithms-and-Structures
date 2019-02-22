# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        # iteration
        # get the head and insert tail
        # if not head:
        #     return head
        # p = head
        # while p.next:
        #     p = p.next
        # q = head
        # while q != p:
        #     temp = q.next
        #     q.next = p.next
        #     p.next = q
        #     q = temp
        # return q
        
        # recursion I
        # if not head or not head.next:
        #     return head
        # p, q = head, head
        # while p.next:
        #     q = p
        #     p = p.next
        # q.next = None
        # p.next = self.reverseList(head)
        # return p
        
        # recursion II
        # use self loop
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
