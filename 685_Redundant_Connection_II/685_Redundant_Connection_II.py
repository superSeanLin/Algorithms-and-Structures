class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # every time meet a new edge and use DFS to see if we can reach the target; or if a node has multiple parents
        # at most one cycle and at most one node with two parents; return intersect
        graph = {}  # node : child
        parent = {}  # node : parent
        mul = None
        for edge in edges:  # first find if mul
            visited = set()
            node1, node2 = edge[0], edge[1]
            if not mul:
                if not node2 in parent:
                    parent[node2] = node1
                elif node1 != parent[node2]:  # multiple parents
                    parent[node2] = [parent[node2], node1]
                    mul = node2
                    break
        for edge in edges:
            visited = set()
            node1, node2 = edge[0], edge[1]
            if mul:
                if not node1 in graph:
                    graph[node1] = [node2]
                else:
                    graph[node1].append(node2)
                for i in range(2):
                    node1, node2 = parent[mul][i], mul
                    if self.DFS(graph, node2, node1, visited):  # if reverse path existed
                        return [node1, node2]
            else:
                if self.DFS(graph, node2, node1, visited):  # if reverse path existed
                    return [node1, node2]
                if not node1 in graph:
                    graph[node1] = [node2]
                else:
                    graph[node1].append(node2)
        return [parent[mul][1], mul]

    def DFS(self, graph, node1, node2, visited):
        if not node1 in graph:
            return False
        if node2 in graph[node1]:
            return True
        visited.add(node1)
        for node3 in graph[node1]:
            if not node3 in visited and node3 in graph:
                return self.DFS(graph, node3, node2, visited)
        return False
