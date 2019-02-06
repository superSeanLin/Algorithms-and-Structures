# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## see idea from discussion
    def __init__(self):
        self.first, self.second = None, None  # compare prev with root
        self.prev = TreeNode(-2**31)
        
    def recoverTree(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if not self.first and self.prev.val >= root.val:
            self.first = self.prev
        if self.first and self.prev.val >= root.val:
            self.second = root
        self.prev = root
        self.traverse(root.right)
