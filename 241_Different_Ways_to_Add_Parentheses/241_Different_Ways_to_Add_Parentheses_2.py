class Solution:
    ## Note: part1 op part2; last op removes duplicates
    def diffWaysToCompute(self, input: str) -> List[int]:
        # n! different way; recursive
        res = self.helper(input)
        return res
    
    def helper(self, input):
        res = []
        if not "+" in input and not "-" in input and not "*" in input:
            return [int(input)]
        for i, char in enumerate(input):
            if char == "+":
                left = self.helper(input[:i])
                right = self.helper(input[i+1:])
                for l in left:
                    for r in right:
                        res.append(l + r)
            elif char == "-":
                left = self.helper(input[:i])
                right = self.helper(input[i+1:])
                for l in left:
                    for r in right:
                        res.append(l - r)
            elif char == "*":
                left = self.helper(input[:i])
                right = self.helper(input[i+1:])
                for l in left:
                    for r in right:
                        res.append(l * r)
        return res
