class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # use DP, like the longest increasing number
        words.sort(key=lambda x: len(x))
        length = {}  # length of word : [words]
        for word in words:
            l = len(word)
            if l not in length:
                length[l] = [word]
            else:
                length[l].append(word)
        mini, maxi = min(length), max(length)
        dp = {}  # {length of word : {word : the longest string chain ending at this word}}
        dp[mini] = {}
        for word in length[mini]:  # base case
            dp[mini][word] = 1
        for i in range(mini+1, maxi+1):
            dp[i] = {}
            for word2 in length[i]:
                temp = 1
                for word1 in length[i-1]:
                    if self.isNext(word1, word2):
                        temp = max(temp, dp[i-1][word1]+1)
                dp[i][word2] = temp
        return max([max(dp[x].values()) for x in dp])

    def isNext(self, word, nxt):
        # check if all the same after skipping one char
        idx = 0
        while idx < len(word) and word[idx] == nxt[idx]:
            idx += 1
        return idx == len(word) or word[idx:] == nxt[idx+1:]

