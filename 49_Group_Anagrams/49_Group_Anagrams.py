class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ## Also can hash by counter of alphabet
        res = []
        index = 0
        words = {}
        for w in strs:
            temp = tuple(sorted(tuple(w)))
            if words.get(temp) is None:  # new combination
                words[temp] = index
                res.append([w])
                index += 1
            else:
                i = words[temp]
                res[i].append(w)
        return res
