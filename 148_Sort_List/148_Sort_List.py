# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    ## Why so slow?
    def sortList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head
        self.quickSort(head, None)
        return head
    
    def quickSort(self, head, end):
        if head == end:
            return
        p = self.partition(head, end)
        self.quickSort(head, p)
        self.quickSort(p.next, end)
        
    def partition(self, head, end):
        pivot = head.val
        idx, p = head, head  # idx: processed node
        temp = p  # store pivot pointer
        while p != end:
            if p.val < pivot:
                if idx.val == pivot:
                    temp = p
                idx.val, p.val = p.val, idx.val
                idx = idx.next
            p = p.next
        temp.val, idx.val = idx.val, temp.val
        return idx
        
