# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## use slow pointer and faster pointer to get middle of the linked list
    ## solution #3 good idea
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        ## first convert into a list?
        elem = []
        if not head:
            return None
        p = head
        while p:
            elem.append(p.val)
            p = p.next
        return self.List2BST(elem)
    
    def List2BST(self, elem):
        if not elem:
            return None
        n = len(elem)
        mid = n//2
        root = TreeNode(elem[mid])
        if mid > 0:
            root.left = self.List2BST(elem[:mid])
        if mid < n:
            root.right = self.List2BST(elem[mid+1:])
        return root
