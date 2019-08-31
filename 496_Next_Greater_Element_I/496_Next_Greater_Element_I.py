class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextLarge = {}  # number : next larger
        stack = []  # descending stack, since
        res = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:  # all smaller should be set
                nextLarge[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for x in nums1:
            if x not in nextLarge:
                res.append(-1)
            else:
                res.append(nextLarge[x])
        return res
                
