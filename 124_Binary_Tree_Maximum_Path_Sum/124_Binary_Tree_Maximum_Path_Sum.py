# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## DFS; root-leaves path not necessary
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        # base cases
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        _, path = self.dfs(root)
        return path
    
    def dfs(self, root):  # left/right may include root; L/R exclude root; all maximum path
        left, right, L, R = 0, 0, root.val, root.val
        if root.left:
            left, L = self.dfs(root.left)
            left = max(left, 0)  # negative never accumulate
        if root.right:
            right, R = self.dfs(root.right)
            right = max(right, 0)
        return max(left, right)+root.val, max(L, R, left+root.val+right)
