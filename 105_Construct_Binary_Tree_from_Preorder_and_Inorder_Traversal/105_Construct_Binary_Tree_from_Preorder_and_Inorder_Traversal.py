# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root.left = None
        root.right = None
        index = inorder.index(root.val)
        if index > 0:
            preorder.pop(0)  # don't redirect the pointer
            root.left = self.buildTree(preorder, inorder[:index])
        if index < len(inorder)-1:
            preorder.pop(0)
            root.right = self.buildTree(preorder, inorder[index+1:])
        return root
