class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ## use stack, while stack.top < curr, process
        l = len(nums)
        if l == 0:
            return []
        res = [-1] * (2*l)
        stack = [0]  # store index
        nums = nums + nums  # circular trick
        for i in range(1, 2*l):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return res[:l]
