import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: 'TreeNode') -> 'List[int]':
    ## use two queue?
        res = []
        if not root:
            return res
        q1, q2 = queue.Queue(), queue.Queue()
        q1.put(root)
        while not q1.empty() or not q2.empty():
            node = None  # mark last one
            while not q1.empty():
                node = q1.get()
                if node.left:
                    q2.put(node.left)
                if node.right:
                    q2.put(node.right)
            if node:
                res.append(node.val)
            node = None
            while not q2.empty():
                node = q2.get()
                if node.left:
                    q1.put(node.left)
                if node.right:
                    q1.put(node.right)
            if node:
                res.append(node.val)
        return res
