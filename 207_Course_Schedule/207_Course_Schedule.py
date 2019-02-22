class Solution:
    # topological sort, first build the connected graph, then see if have sink and able to traverse
    # actually this problem ask if loop
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        # build adjacent martix
        if not prerequisites:
            return True
        adj = {}  # node -> [nei]
        for pair in prerequisites:
            [node1, node2] = pair  # no duplicate edges
            if not node2 in adj:
                adj[node2] = [node1]
            else:
                adj[node2].append(node1)
            if not node1 in adj:
                adj[node1] = []
        order = self.topologicalSortKahn(adj)
        return order
    
    def topologicalSortKahn(self, adj):
        # find sink
        if not adj:
            return True
        sink = 
        for node in adj:
            if not adj[node]:  # empty outgoing edges
                sink = node
                break
        if sink == None:
            return False
        # remove this node from graph
        adj.pop(sink)
        for node in adj:
            if sink in adj[node]:
                adj[node].remove(sink)
        return self.topologicalSortKahn(adj)
    
    def topologicalSortKahnRecurse(self, adj):
        # find sink
        if not adj:
            return True
        sink = None
        for node in adj:
            if not adj[node]:  # empty outgoing edges
                sink = node
                break
        if sink == None:
            return False
        # remove this node from graph
        adj.pop(sink)
        for node in adj:
            if sink in adj[node]:
                adj[node].remove(sink)
        return self.topologicalSortKahn(adj)
    
    def topologicalSortDFS(self, adj):
        # topological sort can start with source or sink; start from sink here (DFS)
        stack = []
        visited = set()
        for node in adj:
            if not node in visited:
                self.helper(adj, node, visited, stack)
        return stack
                
    def helper(self, adj, node, visited, stack):
        visited.add(node)
        if node in adj:  # not sink
            for nei in adj[node]:
                if nei not in visited:
                    self.helper(adj, nei, visited, stack)
        # after all its neighbor, insert it  -> sink first
        stack.insert(0, node)
        
