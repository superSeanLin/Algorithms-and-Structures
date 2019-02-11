# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        return max(self.Numbers(root.left, root.val) + self.Numbers(root.right, root.val), root.val)
    
    def Numbers(self, root, prevSum):
        if not root:
            return 0
        prevSum = prevSum*10 + root.val
        return max(self.Numbers(root.left, prevSum) + self.Numbers(root.right, prevSum), prevSum)  # leaf case
