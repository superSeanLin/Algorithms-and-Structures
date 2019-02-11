class Solution:
    def findLadders(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'List[List[str]]':
        ## build a graph implicit, then BFS
        wordList = set(wordList)  # use set to save time
        res = [[beginWord]]
        if not endWord in wordList:
            return []
        visited = {beginWord:[]}
        prev = set([beginWord])
        while not endWord in prev:
            #print(prev, visited, res)
            wordList -= prev
            prev = self.update(prev, wordList, visited)
            if not prev:
                return []
            if endWord in prev:
                prev = [endWord]
            res = self.concatenate(res, prev, visited)
        return res
    
    def update(self, prev, wordList, visited):
        ans = set()
        for word in prev:
            for i in range(len(word)):
                for ch in range(97, 123):
                    ch = chr(ch)
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord != word and newWord in wordList and not newWord in visited:
                        ans.add(newWord)
                        visited[word].append(newWord)
        for word in ans:
            visited[word] = []
        return ans
        
    def concatenate(self, res, prev, visited):
        newRes = []
        for path in res:
            last = path[-1]
            for word in visited[last]:
                if word in prev:
                    newRes.append(path+[word])
        return newRes
