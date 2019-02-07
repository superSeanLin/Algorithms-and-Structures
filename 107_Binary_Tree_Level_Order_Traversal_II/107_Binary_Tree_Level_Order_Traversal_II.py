import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        ans = []
        if not root:
            return ans
        isChild = 0
        prev = 1
        q = queue.Queue()
        q.put((root, isChild))
        while not q.empty():
            node, isChild = q.get()
            if isChild != prev:
                ans = [[]] + ans
                prev = isChild
            ans[0].append(node.val)
            if node.left:
                q.put((node.left, 1-isChild))
            if node.right:
                q.put((node.right, 1-isChild))
        return ans
