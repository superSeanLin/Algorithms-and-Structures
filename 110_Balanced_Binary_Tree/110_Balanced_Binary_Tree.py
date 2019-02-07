# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        return self.check(root)[0]
    
    def check(self, root):
        if not root:
            return True, 0
        LB, left = self.check(root.left)
        RB, right = self.check(root.right)
        if LB and RB and abs(left-right) <= 1:
            return True, 1+max(left, right)
        else:
            return False, 1+max(left, right)
