# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        if not root:
            return res
        prev = None  # store last pop
        stack = []
        self.addLeft(root, stack)
        while stack:
            top = stack[-1]
            if prev == top.right or not top.right:  # right pop or leaf; right finished then pop the root
                node = stack.pop()
                res.append(node.val)
                prev = node
            else:
                self.addLeft(top.right, stack)
        return res
    
    def addLeft(self, root, stack):
        while root:
            stack.append(root)
            root = root.left
