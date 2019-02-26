class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        idx = 0  # start of window
        window = {}  # type : last index
        length = 0  # max length
        for i in range(len(tree)):
            if not tree[i] in window:  # new type
                if len(window) >= 2:
                    pop, last_index = None, 0
                    for j in window:  # find the which should be pop
                        if pop == None or window[j] < last_index:
                            pop, last_index = j, window[j]
                    idx = window[pop]  # reassign start of window
                    del window[pop]
                window[tree[i]] = i+1  # careful about index here
            else:
                window[tree[i]] = i+1
            length = max(length, i-idx+1)
        return length

