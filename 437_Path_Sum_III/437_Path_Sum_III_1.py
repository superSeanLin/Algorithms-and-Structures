# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        book = {0:1}  # keep path sums
        path = self.dfs(root, 0, sum, book)
        return path
    
    def dfs(self, root, temp, sum, book):
        path = 0
        if not root:
            return path
        temp += root.val
        if not temp in book:
            book[temp] = 1
        else:
            book[temp] += 1
        path += self.dfs(root.left, temp, sum, book)
        path += self.dfs(root.right, temp, sum, book)
        book[temp] -= 1  # don't affact the other subtree when backtracing
        if temp-sum in book:
            path += book[temp-sum]
        return path
        
