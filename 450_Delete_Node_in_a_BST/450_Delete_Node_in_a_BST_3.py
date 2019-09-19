# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## method 3: recursive replacement method
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key > root.val:  # right child
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:  # left child
            root.left = self.deleteNode(root.left, key)
            return root
        else:  # key == root.val
            if not root.left:  # this will include case root is leaf
                return root.right
            elif not root.right:
                return root.left
            else:  # both vaild; replace leftmost of right child
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)  # delete swapped node
            return root
