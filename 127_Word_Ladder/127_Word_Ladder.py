class Solution:
    ## naive method; tried dictionary-tree; maybe BFS/DFS
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        if not endWord in wordList:
            return 0
        step = set(endWord)
        count = 1
        prev = [endWord]
        while not self.changable(beginWord, prev):
            prev = self.diffOne(prev, wordList, step, count)
            if not prev:  # not valid
                return 0
            count += 1
        return count+1
    
    def changable(self, beginWord, prev):  # return if beginWord can change to one word in prev within one step
        n = len(beginWord)
        for word in prev:
            dis = 0
            for i in range(n):
                if beginWord[i] != word[i]:
                    dis += 1
                if dis >= 2:
                    break
            if dis <= 1:
                return True
        return False
            
    def diffOne(self, prev, wordList, step, count):
        res = []
        for word in wordList:
            if (not word in step) and self.changable(word, prev):
                res.append(word)
        for word in res:
                if not word in step:  # keep minimum
                    step.add(word)
        return res
