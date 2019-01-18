# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    ## Use heap to do better job
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minimum = 1000
        p = None
        for l in lists:  # find min of all lists
            if l and l.val < minimum:
                p = l
                minimum = l.val
        if p:  # not all None
            q = p
            lists[lists.index(p)] = p.next  # change original lists
            q.next = self.mergeKLists(lists)
            return q
        else:  # all None
            return None
