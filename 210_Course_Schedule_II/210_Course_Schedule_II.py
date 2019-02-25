class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
	# build a graph, start with sink to output the topological sort; when there is no sink but still have remaining nodes in graph, there is no possible topological sort
        res = []	
        if not numCourses:
            return res
        if not prerequisites:
            return list(range(numCourses))
        graph = self.construct(prerequisites)  # course -> prerequiests
        res = self.topoSort(graph, numCourses)
        return res

    def construct(self, prerequisites):  # O(N), N is number of edge in graph
        graph = {}  # node -> other end outgoing edge; sink -> []
        for p in prerequisites:
            node1, node2 = p[0], p[1]
            if not node1 in graph:
                graph[node1] = [node2]
            else:
                graph[node1].append(node2)
            if not node2 in graph:
                graph[node2] = []
        return graph

    def topoSort(self, graph, numCourses):  # Khan, remove sinks and the edge conneting them
        # try iteration method
        res = []
        aux = list(range(numCourses))
        while graph:  # O(M*(2M+N)) -> O(M^2+MN)
            sink = None
            for node in graph:  # O(M), M is number of the nodes
                if not graph[node]:
                    sink = node
                    break
            if sink == None:  # no valid sink, cycle
                return []
            res.append(sink)
            aux.remove(sink)
            del graph[sink]  # remove from graph
            for node in graph:  # O(M+N)
                if sink in graph[node]:
                    graph[node].remove(sink)
        return aux + res

