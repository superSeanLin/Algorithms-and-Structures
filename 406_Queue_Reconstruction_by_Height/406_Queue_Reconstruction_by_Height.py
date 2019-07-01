class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ## first sort, then greedily insert; O(n^2)
        # people = sorted(people, key=lambda x:(-x[0], x[1]))  # x[0] descending, x[1] ascending
        # res = []
        # for [currH, currK] in people:
        #     count = 0
        #     idx = len(res)-1
        #     for i, [h, _] in enumerate(res):
        #         if h >= currH:
        #             count += 1
        #         if count == currK:  # break here since no smaller
        #             idx = i + 1
        #             break
        #         if count > currK:
        #             idx = i
        #             break
        #     # insert here
        #     res.insert(idx, [currH, currK])
        # return res
        
        # revised version
        people.sort(key=lambda x:(-x[0], x[1]))  # x[0] descending, x[1] ascending
        res = []
        # note: if in the current list, h is the smallest number, then k in the index of h in the currect list; since there is no smaller numbers
        # in the other word, k is the minimum index of h in the global list
        for [h, k] in people:
            res.insert(k, [h, k])
        return res            
