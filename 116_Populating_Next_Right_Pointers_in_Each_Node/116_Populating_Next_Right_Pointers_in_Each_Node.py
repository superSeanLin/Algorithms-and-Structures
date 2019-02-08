# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    
    ## level order traverse
    def connect(self, root):
        if not root:
            return
        s1, s2 = [root], []
        while len(s1) or len(s2):
            prev = None
            while len(s1):
                node = s1.pop()
                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)
                if prev:
                    prev.next = node
                prev = node
            nxt = None
            while len(s2):
                node = s2.pop()
                if node.right:
                    s1.append(node.right)
                if node.left:
                    s1.append(node.left)
                if nxt:
                    node.next = nxt
                nxt = node
        return
