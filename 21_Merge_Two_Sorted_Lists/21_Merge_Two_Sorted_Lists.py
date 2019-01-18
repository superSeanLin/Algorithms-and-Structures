# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
## Use recursion, each time branch out one node
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:  # l1 None
            return l2
        if not l2:  # l2 None
            return l1
        if l1.val < l2.val:
            temp = l1.next
            l1.next = self.mergeTwoLists(temp, l2)
            return l1
        else:
            temp = l2.next
            l2.next = self.mergeTwoLists(l1, temp)
            return l2
