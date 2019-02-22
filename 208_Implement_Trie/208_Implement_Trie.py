class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False  # mark if end of the word
        self.child = [None] * 26  # can do better there
        
    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        n = len(word)
        child = self.child
        for i in range(n):
            idx = ord(word[i]) - ord('a')
            node = child[idx]
            if not node:  # empty child node
                node = Trie()
                child[idx] = node
            child = node.child
        node.isEnd = True
            
    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        n = len(word)
        child = self.child
        for i in range(n):
            idx = ord(word[i]) - ord('a')
            node = child[idx]
            if not node:
                return False
            child = node.child
        if not node.isEnd:
            return False
        return True
        

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = len(prefix)
        child = self.child
        for i in range(n):
            idx = ord(prefix[i]) - ord('a')
            node = child[idx]
            if not node:
                return False
            child = node.child
        return True
    
    def isEmpty(self, child):
        for c in child:
            if c:
                return False
        return True
    
    def delete(self, word: 'str', depth: int) -> 'None':
        if depth == len(word):  # end of the word
            if self.isEnd:
                self.isEnd = False
            if self.isEmpty(self.child):  # not prefix of other word
                del self
        idx = ord(word[depth]) - ord('a')
        if self.child[idx]:
            self.child[idx].delete(word, depth+1)
        if self.isEmpty(self.child) and not self.isEnd:
            del self
            
                

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
