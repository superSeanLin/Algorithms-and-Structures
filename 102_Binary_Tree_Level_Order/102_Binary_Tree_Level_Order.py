import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        ## iterative method with queue
        ans = []
        if not root:
            return ans
        isChild = 0  # flag for next generation
        prev = 1
        q = queue.Queue()
        q.put((root, isChild))
        while not q.empty():
            node, isChild = q.get()
            if prev != isChild:
                ans.append([])
                prev = isChild
            ans[-1].append(node.val)
            if node.left:
                q.put((node.left, 1-isChild))
            if node.right:
                q.put((node.right, 1-isChild))
        return ans
