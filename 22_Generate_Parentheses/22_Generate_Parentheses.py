class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Dynamic Programming like
        res = [[] for i in range(n+1)]
        res[1] = ["()"]
        if n == 0:
            return res[0]
        if n == 1:
            return res[1]
        for count in range(2, n+1):
            temp = set()
            x = 1
            while x <= count // 2:  # x + y = count
                y = count - x
                for xs in res[x]:
                    for ys in res[y]:
                        temp.add(xs[0] + ys + xs[1:])
                        #temp.add(xs[:-1] + ys + xs[-1])
                        temp.add(xs + ys)
                        temp.add(ys + xs)
                x += 1
            res[count] = list(temp)
        return res[n]
