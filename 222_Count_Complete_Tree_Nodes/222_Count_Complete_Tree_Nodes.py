# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        ## level-order traverse, find less-child on the last second layer
        ## also use recursive method to find full binary tree (left_height == right_height)
        if not root:
            return 0
        flag = 0
        q = [(root, flag)]
        height = 1
        layer_count = 0
        right = 0  # indicate if left child exists
        while q:
            (node, f) = q.pop(0)
            if f != flag:  # new layer
                flag = f
                height += 1
                layer_count = 0
            if node.left:
                q.append((node.left, 1-f))
                if node.right:
                    q.append((node.right, 1-f))
                else:  # no right child
                    right = 1
                    break
            else:  # no left child
                break
            layer_count += 1
        return 2**height + 2 * layer_count + right - 1
