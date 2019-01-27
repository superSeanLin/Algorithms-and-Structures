# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## remember to use helper function if it wants in-place modification
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:  # void root
            return
        self.helper(root)
    
    def helper(self, root):
        if not root:  # void root
            return None
        left_child = root.left
        right_child = root.right
        root.left = None
        root.right = self.helper(left_child)
        temp = root
        while temp.right:
            temp = temp.right  # last right child
        temp.right = self.helper(right_child)
        return root
