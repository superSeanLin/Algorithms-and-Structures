# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ## use fast, slow pointers to find the middle point and compare 
        if not head:
            return True
        rev = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next  # redirect
        if fast:
            slow = slow.next  # leave middle alone
        while slow and rev:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
        return True
