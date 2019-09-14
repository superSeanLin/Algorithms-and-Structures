class Solution:
    # DP, store all preprocessed result x < n
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        res = {0: [""], 1: ["()"]}
        for count in range(2, n+1):
            temp = []
            for x in range(count):  # trick here is to use x from [0, count], which will reverse the sequence somehow, and use (xs)ys will not generate duplicates
                y = count - x - 1
                for xs in res[x]:
                    for ys in res[y]:
                        temp.append('(' + xs + ')' + ys)
            res[count] = temp
        return res[n]
