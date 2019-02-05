# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ## devide and conquer; queue / BFS / layer traverse
        ## Note: with help of TreeNode!!!
        if n < 1:
            return []
        res = self.uniqueBST(1, n)
        return res
    
    def uniqueBST(self, min, max):
        res = []
        if min > max:
            return [None]
        if min == max:
            leaf = TreeNode(min)
            return [leaf]
        for i in range(min, max+1):
            left = self.uniqueBST(min, i-1)
            right = self.uniqueBST(i+1, max)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
