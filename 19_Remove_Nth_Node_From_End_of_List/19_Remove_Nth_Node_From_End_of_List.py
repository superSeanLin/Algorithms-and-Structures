# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1, p2 = head, head
        for i in range(n):  # make sure p1 - p2 = n; n always valid
            p1 = p1.next
        if not p1:  # n = len(list)
            return head.next
        while p1.next != None:  # until reach tail
            p1 = p1.next
            p2 = p2.next
        temp = p2.next
        p2.next = temp.next
        #temp.next = None
        return head
        
        
