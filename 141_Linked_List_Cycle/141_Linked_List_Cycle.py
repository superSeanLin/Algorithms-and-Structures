# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## fast and slow pointer
        slow, fast = head, head
        while fast:
            fast = fast.next
            if not fast:  # reach end
                break
            fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
        return False
            
