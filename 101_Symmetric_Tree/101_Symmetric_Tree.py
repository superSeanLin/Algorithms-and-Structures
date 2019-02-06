# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        if (not root.left and root.right) or (not root.right and root.left):
            return False
        return self.isSame(root.left, root.right)
    
    def isSame(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.isSame(left.left, right.right) and self.isSame(left.right, right.left)
