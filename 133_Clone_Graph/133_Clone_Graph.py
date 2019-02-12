import Queue
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    ## also may try recursive method
    def cloneGraph(self, node):
        if not node:
            return node
        res = UndirectedGraphNode(node.label)
        parent = Queue.Queue()  # keep (originNode, cloneNode) in queue; only contain non-visited
        parent.put((node, res))
        visited = {}  # originNode : cloneNode
        while not parent.empty():
            p = parent.get()
            origin = p[0]
            clone = p[1]
            visited[origin] = clone
            for c in origin.neighbors:
                nei = None
                if not c in visited:
                    nei = UndirectedGraphNode(c.label)
                    parent.put((c, nei))  # if node already built, then all its neighbors built
                else:  # already have a copy
                    nei = visited[c]
                clone.neighbors.append(nei)
        return res
                    
                
