class Solution:
    def __init__(self):
        self.itin = None
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build graph, use DFS with lexical order to find Eulerian path
        # use DFS until end and backtracking; backtracking let cycle merged
        if not tickets:
            return []
        #graph  = self.build(tickets)
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            graph[a] += b,
        #self.dfs(graph, "JFK", ["JFK"])
        itin = self.dfs(graph)
        return itin
    
    def build(self, tickets):  # BFS with stack???
        graph = {}  # node : child
        for pair in tickets:
            start, end = pair[0], pair[1]
            if not start in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)
            if not end in graph:
                graph[end] = []
        for start in graph:
            graph[start] = sorted(graph[start])
        return graph
    
    def dfs(self, graph):
        res = []
        stack = ["JFK"]
        while stack:
            if stack[-1] in graph:
                while graph[stack[-1]]:
                    stack += graph[stack[-1]].pop(),  # "," changes string to tuple
            res += stack.pop(),  # res += "JFK" -> ["J","F","K"]; res += ("JFK",) -> ["JFK"]
        return res[::-1]


#     def dfs(self, graph, node, path):
#         if not graph:  # terminate
#             if not self.itin:
#                 self.itin = path[:]
#             else:
#                 self.itin = min(self.itin, path)
#         if not node in graph:  # not valid path
#             return
#         temp = graph[node][:]
#         for child in temp:
#             graph[node].remove(child)
#             if not graph[node]:
#                 del graph[node]
#             self.dfs(graph, child, path+[child])
#             graph[node] = temp[:]  # compensate
#         return
