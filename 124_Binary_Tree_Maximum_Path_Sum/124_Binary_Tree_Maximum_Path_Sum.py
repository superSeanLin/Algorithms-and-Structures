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
        left, right, L, R = self.dfs(root)
        return max(left, right, left+right-root.val, L, R)
    
    def dfs(self, root):  # left/right may include root; L/R exclude root; all maximum path
        if not root.left and not root.right:  # stop at leaves
            return root.val, root.val, root.val, root.val
        left, right, L, R = -2**31, -2**31, -2**31, -2**31
        if root.left:
            ll, lr, lL, lR = self.dfs(root.left)
            left = max(max(ll, lr), root.left.val)
            L = max(lL, lR, ll+lr-root.left.val, left)
        if root.right:
            rl, rr, rL, rR = self.dfs(root.right)
            right = max(max(rl, rr), root.right.val)
            R = max(rL, rR, rl+rr-root.right.val, right)
        return max(left+root.val, root.val), max(right+root.val, root.val), L, R
