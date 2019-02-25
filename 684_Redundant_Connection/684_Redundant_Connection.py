class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # detect the cycle in the undirected graph
        
        # method 1: union-find; if nodes are in different sets, union them; if nodes are in the same set, then cycle
        s = {}  # node : set
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            if not node1 in s and not node2 in s:  # new set
                s[node1] = set([node1, node2])
                s[node2] = s[node1]
            elif not node2 in s:
                s[node1].add(node2)
                s[node2] = s[node1]
            elif not node1 in s:
                s[node2].add(node1)
                s[node1] = s[node2]
            elif s[node1] != s[node2]:
                s[node1].update(s[node2])
                for node in s[node2]:
                    s[node] = s[node1]  # reassign
            elif s[node1] == s[node2]:
                return edge
                
        # method 2: DFS; find a vertex whose neighbor is visited but not its parent; but how to keep the order
        # graph = self.construct(edges)
        # return self.DFS(graph)
        
    def construct(self, edges):
        graph = {}  # node : child
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            if not node1 in graph:
                graph[node1] = [node2]
            else:
                graph[node1].append(node2)
            if not node2 in graph:
                graph[node2] = [node1]
            else:
                graph[node2].append(node1)
        return graph
    
    def DFS(self, graph):
        visited = set()  # mark visited nodes
        parent = {}  # node : parent
        stack = [1]
        while stack:
            top = stack[-1]
            for nxt in graph[top]:
                if nxt in visited and parent[top] != nxt:
                    return [[top, nxt], [nxt, top]][nxt < top]
                if not nxt in visited:
                    stack.append(nxt)
                    parent[nxt] = top
            top = stack.pop()
            visited.add(top)
                    
