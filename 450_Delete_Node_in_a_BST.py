# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## method 1: find its successor and replace the value, finally delete the leaf
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:  # empty one
            return root
        q, p = root, root  # q = p.prev; used to find the deleting node
        while p and p.val != key:  # stop when find the node
            q = p
            if key > p.val:
                p = p.right
            else:
                p = p.left
        if not p:  # key not exist
            return root
        # find its successor, it is either the leftmost of right child or rightmost of left child
        if p.left:  # find the rightmost leaf
            parent, leaf = p, p.left  # parent = leaf.prev
            while leaf.right:
                parent = leaf
                leaf = leaf.right
            p.val = leaf.val  # replace the value
            # now we need to delete the leaf
            if p == parent:  # no right child
                parent.left = leaf.left
            else:  # right child valid
                parent.right = leaf.left
            del leaf  ## Note: del in python just release reference from object
        elif p.right:
            parent, leaf = p, p.right  # parent = leaf.prev
            while leaf.left:
                parent = leaf
                leaf = leaf.left
            p.val = leaf.val  # replace the value
            # now we need to delete the leaf
            if p == parent:  # no left child
                parent.right = leaf.right
            else:  # left child valid
                parent.left = leaf.right
            del leaf
        else:  # leaf node
            if p == root:  # remove root and no children
                return None
            if q.left == p:
                q.left = None
            else:
                q.right = None
            del p
        return root
