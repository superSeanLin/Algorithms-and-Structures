# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        if not postorder:
            return None
        root = TreeNode(postorder.pop())
        root.left = None
        root.right = None
        idx = inorder.index(root.val)
        if idx < len(inorder)-1:
            root.right = self.buildTree(inorder[idx+1:], postorder)
        if idx > 0:
            root.left = self.buildTree(inorder[:idx], postorder)
        return root
