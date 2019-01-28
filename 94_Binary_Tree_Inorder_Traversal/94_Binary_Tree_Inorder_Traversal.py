# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        res = []
        stack = []
        stack.append(root)
        temp = root.left
        while temp:
            stack.append(temp)
            temp = temp.left
        last = None
        while len(stack) > 0:
            last = stack[-1]  # only when left child done, then pop
            stack.pop()
            res += [last.val]
            temp = last.right
            while temp:
                stack.append(temp)
                temp = temp.left
        return res
