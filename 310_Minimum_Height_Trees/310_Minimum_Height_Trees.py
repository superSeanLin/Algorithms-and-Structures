class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## classical: first find the diameter of the tree, using DFS of random node, always ending on a leaf, 
        ## and the use leaf to do DFS, ending on the other leaf (farest from the prev leaf); then use BFS to get diameter/2
        
        ## start from each leaf, do BFS; when meet or 2 node with 1 distance away left
        leaves, graph = self.build(n, edges)
        visited = set()  # visited ==> remove from the graph
        queue = list(leaves)  # only contain non-visited and non-seen nodes
        while n - len(visited) > 2:  # until only two or less nodes left
            num = len(queue)
            for i in range(num):  # process all new nodes; level traversal
                node = queue.pop(0) 
                visited.add(node)
                for child in graph[node]:
                    graph[child].remove(node)
                    if len(graph[child]) == 1:  # only append when child become a leaf
                        queue.append(child)
        return queue
        
    def build(self, n, edges):
        leaves = set(range(n))
        graph = {}  # node : [child]
        for (x, y) in edges:
            if not x in graph:
                graph[x] = [y]
            else:  # seen before, not the leaf
                graph[x].append(y)
                if x in leaves:
                    leaves.remove(x)
            if not y in graph:
                graph[y] = [x]
            else:
                graph[y].append(x)
                if y in leaves:
                    leaves.remove(y)
        return leaves, graph
