# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = []
        
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        if not root:
            return self.ans
        self.path(root, sum, [])
        return self.ans
    
    def path(self, root, sum, path):
        if not root:
            return
        if not root.left and not root.right:
            if root.val == sum:
                path = path + [root.val]
                self.ans.append(path)
                return
            else:
                return
        sum -= root.val
        path = path + [root.val]  # use other memory space to help recurse
        self.path(root.left, sum, path) 
        self.path(root.right, sum, path)
