# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        left_child = self.invertTree(root.left)
        right_child = self.invertTree(root.right)
        root.right = left_child
        root.left = right_child
        return root
