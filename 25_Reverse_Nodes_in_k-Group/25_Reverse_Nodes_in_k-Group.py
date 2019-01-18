# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # naive solution
        i = 0
        temp = head  # last pointer in this round
        p = [temp]
        while i < k-1 and temp:  # multiple of k
            temp = temp.next
            p.append(temp)
            i += 1
        if not temp:  # out of tail
            return head
        head_next = temp.next  # store next head first
        for i in range(len(p)-1, 0, -1):  # reverse
            p[i].next = p[i-1]
        p[0].next = self.reverseKGroup(head_next, k)
        return p[-1]
