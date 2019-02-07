import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        ## could use two stacks / deck; also can use reserve
        ans = []
        if not root:
            return ans
        s1, s2 = [], [root]
        rnd = 0
        while len(s1) != 0 or len(s2) != 0:
            ans.append([])
            if rnd % 2 == 0:  # even round
                while len(s2) != 0:
                    node = s2.pop()
                    ans[-1].append(node.val)
                    if node.left:
                        s1.append(node.left)
                    if node.right:
                        s1.append(node.right)
                rnd += 1
            else:  # odd round            
                while len(s1) != 0:
                    node = s1.pop()
                    ans[-1].append(node.val)
                    if node.right:
                        s2.append(node.right)
                    if node.left:
                        s2.append(node.left)
                rnd += 1
        return ans
