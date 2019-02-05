# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        return self.check(root)[0]
    
    def check(self, root):
        if not root:
            return True, None, None
        if not root.left and not root.right:
            return True, root.val, root.val
        if not root.left or root.left.val < root.val:
            left, lmin, lmax = self.check(root.left)
        else:
            return False, None, None
        if not root.right or root.right.val > root.val:
            right, rmin, rmax = self.check(root.right)
        else:
            return False, None, None
        return left and (not lmax or lmax < root.val) and right and (not rmin or rmin > root.val), lmin, rmax
        
