# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: 'ListNode') -> 'None':
        """
        Do not return anything, modify head in-place instead.
        """
        ## naive solution
        if not head:
            return head
        prev = {head:None}  # next:prev
        p, q = head, head  # q is prev of p
        while p.next:
            p = p.next
            prev[p] = q
            q = p
        q = head  # now p is the last one
        while p and q and p != q:  # not the same; q/p
            temp1 = q.next
            temp2 = temp1.next
            if temp1 == p:  # q->p
                break
            q.next = p
            p.next = temp1
            if temp1 != prev[p]:
                temp1.next = prev[p]
                q = temp2
                if temp2 != prev[p]:
                    prev[p].next = q
                    p = prev[prev[p]]  
                    if p == q:  # q->x->y->z->p
                        q.next = None
                        break
                else:  # q->x->y->p
                    q.next = None
                    break
            else:  # q->x->p
                temp1.next = None
                break
