# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # level-order traverse
        if not root:
            return ""
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node != None:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
        # truncate
        while res[-1] == None:
            res.pop()
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # only complete binary tree can apply child indices -> i*2+1, i*2+2
        # use existing node to find its parents
        if not data:
            return None
        data = eval(data)  # change string back to list
        root = TreeNode(data[0])
        parent = [root]
        i = 1
        while i < len(data):
            p = parent.pop(0)  # queue
            if data[i] != None:
                node = TreeNode(data[i])
                p.left = node
                parent.append(node)
            i += 1
            if i < len(data) and data[i] != None:
                node = TreeNode(data[i])
                p.right = node
                parent.append(node)
            i+=1
        return root
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
