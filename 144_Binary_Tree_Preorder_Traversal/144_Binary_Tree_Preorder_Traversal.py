# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        if not root:
            return res
        stack = []
        self.addLeft(stack, root, res)
        while stack:
            node = stack.pop()
            if node.right:
                self.addLeft(stack, node.right, res)
        return res
    
    def addLeft(self, stack, root, res):
        while root:
            stack.append(root)
            res.append(root.val)
            root = root.left
        
