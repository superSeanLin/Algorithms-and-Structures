import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Dijkstra like, use min heap; also backtracking
        graph = self.build(flights)
        if not src in graph:
            return -1  # src no out degree
        queue = [(0, src, K+1)]
        while queue:
            (dist, node, stop) = heapq.heappop(queue)
            if node == dst:  # first destination
                return dist
            if stop <= 0:
                continue
            # relax
            # if not node in graph[src]:
            #     graph[src][node] = dist
            # else:
            #     graph[src][node] = min(dist, graph[src][node])
            for child in graph[node]:
                heapq.heappush(queue, (dist+graph[node][child], child, stop-1))
        return -1
    
    def build(self, flights):
        graph = {}  # node : {node:dist}
        for pair in flights:
            (start, end, edge) = pair
            if not start in graph:
                graph[start] = {end: edge}
            else:
                graph[start][end] = edge
        return graph
