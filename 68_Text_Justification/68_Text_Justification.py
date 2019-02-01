class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ## very ugly solution
        n = len(words)
        idx = 0  # processed index
        res = []
        while idx < n:
            length = len(words[idx])
            count = 1
            for i in range(idx+1, n):
                if length + 1 + len(words[i]) > maxWidth:  # 1 for space
                    break
                count += 1
                length = length + 1 + len(words[i])
            num_space = maxWidth - length
            s = ""
            if n-1 - idx < count:  # last line
                while count:
                    if count == 1:
                        s += words[idx]
                        s += " " * num_space
                        break
                    s += words[idx] 
                    s += " "
                    count -= 1
                    idx += 1
            else:
                while count:
                    if count == 1:
                        s += words[idx]  # last idx
                        s += " " * num_space
                        break
                    if num_space % (count-1) != 0:  # can not devide
                        p = num_space // (count-1)
                        num_space -= (p + 1)
                        s = s + words[idx] + " " * (2 + p)
                        count -= 1
                    else:
                        p = num_space // (count-1)
                        num_space -= p
                        s = s + words[idx] + " " * (1 + p)
                        count -= 1
                    idx += 1
            res.append(s)
            idx += 1
        return res
