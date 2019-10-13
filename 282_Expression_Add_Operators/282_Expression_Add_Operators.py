class Solution:
    def __init__(self):
        self.res = []
        
    def addOperators(self, num: str, target: int) -> List[str]:
        # backtracking
        n = len(num)
        # prev is previous opeartion, curr is current keeping element, acc is current accumulated value
        # temp is the total string, start is the index of num
        def helper(start, prev, curr, acc, temp):
            if start == n:
                if acc == target and curr == 0:  # use all digits; since no opeartor option can leak some digits out
                    print(prev, curr, acc, temp)
                    self.res.append(temp[1:])  # remove leading '+'
                return
            curr = curr*10 + int(num[start])
            helper(start+1, curr, 0, acc+curr, temp+"+"+str(curr))
            if temp:  # not uniary
                helper(start+1, -curr, 0, acc-curr, temp+"-"+str(curr))
                helper(start+1, prev*curr, 0, acc-prev+prev*curr, temp+"*"+str(curr))
            if curr > 0:  # do not start with 0; insert nothing
                helper(start+1, prev, curr, acc, temp)
        helper(0, 0, 0, 0, "")
        return self.res
