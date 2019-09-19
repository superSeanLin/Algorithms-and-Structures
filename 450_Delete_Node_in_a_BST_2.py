# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## method 2: rotation
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        q, p = root, root  # q is parent of p; 
        while p and p.val != key:
            q = p
            if key > p.val:
                p = p.right
            else:
                p = p.left
        if not p:  # key not exist
            return root
        newChild = None
        if p.left and p.right:  # both child valid
            # do rotation; here we always use right child as new root
            left, right = p.left, p.right
            if right.left:  # right child has left child
                temp = left
                while temp.right:  # rightmost of the left child
                    temp = temp.right
                temp.right = right.left
            right.left = left
            newChild = right
        elif p.left and not p.right:  # empty right child
            newChild = p.left
        elif p.right and not p.left:  # empty left child
            newChild = p.right
        else:  # no child
            newChild = None
        # rotation
        if q.left == p:
            q.left = newChild
        else:
            q.right = newChild
        if p == root:  # remove root
            return p.right
        return root
