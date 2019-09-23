class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use ascending stack; if we meet a lower height, then previous height is useless since the highest should be update;
        # and using ascending stack guarantees all after > using height
        stack = [-1]  # [index], trick here: set boundery, and so we can discard higher height
        heights.append(0)  # trick here: evaluate in the last stage
        maxi = 0
        for idx, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:  # accumulate previous higher height
                pre = stack.pop()
                dis = idx - stack[-1] - 1
                maxi = max(maxi, dis*heights[pre])
            stack.append(idx)  # now all height in stack <= h
        return maxi
        
                
