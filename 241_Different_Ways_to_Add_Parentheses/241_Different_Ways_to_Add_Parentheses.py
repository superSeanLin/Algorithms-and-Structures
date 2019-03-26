class Solution:
    ## Note: not decent, should try the other way: part1 op part2; should remove duplicates
    def diffWaysToCompute(self, input: str) -> List[int]:
        # n! different way; use eval(); recursive
        res = [eval(exp) for exp in self.helper(input)]
        return res
    
    def helper(self, input):
        operator = []  # index of operator
        for idx, char in enumerate(input):
            if char in ('+', '-', '*') and idx > 0 and not input[idx-1] in ("+", "-", "*"):  # leave neagtive sign alone
                operator.append(idx)
        n = len(operator)  # number of operator
        if n <= 1:
            return set([input])
        expression = set()  # last expression set, remove duplicates
        for i in range(n):
            if i == 0:
                temp = str(eval(input[:operator[1]])) + input[operator[1]:]
            elif i == n-1:
                temp = input[:operator[n-2]+1] + str(eval(input[operator[n-2]+1:]))
            else:
                temp = input[:operator[i-1]+1] + str(eval(input[operator[i-1]+1:operator[i+1]])) + input[operator[i+1]:]
            expression.update(self.helper(temp))
        return expression
