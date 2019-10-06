class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # first build graph and then use dfs to find the longest path
        graph, start = self.build(words)  # node : [next node]
        path = self.dfs(graph, start)
        return path
    
    def build(self, words):
        length = {}  # length of word : [words]
        graph = {}
        start = set(words)
        for word in words:
            l = len(word)
            if l not in length:
                length[l] = [word]
            else:
                length[l].append(word)
        for word in words:
            l = len(word)
            graph[word] = []
            if l+1 in length:  # not for maximum length
                for nxt in length[l+1]:
                    if self.isNext(word, nxt):
                        graph[word].append(nxt)
                        if nxt in start:
                            start.remove(nxt)  # child of a node
        return graph, start

    def isNext(self, word, nxt):
        # check if all the same after skipping one char
        idx = 0
        while idx < len(word) and word[idx] == nxt[idx]:
            idx += 1
        return idx == len(word) or word[idx:] == nxt[idx+1:]

    def dfs(self, graph, start):
        if len(start) == 0:  # no child
            return 0
        temp = 0
        for word in start:
            temp = max(temp, 1 + self.dfs(graph, graph[word]))
        return temp
