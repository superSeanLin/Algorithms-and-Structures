# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## use two recursive function, one means start accumulation here, one also cares left/right child
    ## also can use dict to keep every path sum and use math
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        path = self.dfs(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return path
    
    def dfs(self, root, temp, sum):
        path = 0
        if not root:
            return path
        temp += root.val
        if temp == sum:
            path += 1
        path += self.dfs(root.left, temp, sum)
        path += self.dfs(root.right, temp, sum)
        return path
        
