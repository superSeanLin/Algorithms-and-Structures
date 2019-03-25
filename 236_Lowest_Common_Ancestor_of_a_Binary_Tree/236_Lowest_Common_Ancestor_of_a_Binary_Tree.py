# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or p.left == q or p.right == q:  # greedy since p, q same subtree
            return p
        if root == q or q.left == p or q.right == p:
            return q
        if self.isChild(root.left, p):
            if self.isChild(root.right, q):  # p left, q right
                return root
            else:
                return self.lowestCommonAncestor(root.left, q, p)  # p, q left
        if self.isChild(root.right, p):
            if self.isChild(root.left, q):  # p right, q left
                return root
            else:
                return self.lowestCommonAncestor(root.right, q, p)  # p, q right
    
    def isChild(self, p, q):
        if p == q:
            return True
        if not p:  # None
            return False
        return self.isChild(p.left, q) or self.isChild(p.right, q)
