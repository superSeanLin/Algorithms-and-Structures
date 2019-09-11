class Solution:
    def trap(self, height: List[int]) -> int:
        ## intuition: find left max and right max to calculate
        
        ## use DP; find maximum height on the left and maximum height on the right for each index
#         if not height:
#             return 0
#         n = len(height)
#         left, right = [0]*n, [0]*n
#         left[0] = height[0]
#         for i in range(1, n):
#             left[i] = max(height[i], left[i-1])  # when unbounded, like index 0, it will use itself
#         right[-1] = height[-1]
#         for i in range(n-2, -1, -1):
#             right[i] = max(height[i], right[i+1])
#         res = 0
#         for i in range(n):
#             res += (min(left[i], right[i]) - height[i])
#         return res
        
        ## use stack 
        # index = []  # store height index; descending stack
        # res = 0
        # for i in range(len(height)):
        #     while len(index) > 0 and height[i] > height[index[-1]]:  # if current > prev, could trap water
        #         top = index.pop()
        #         if len(index) == 0:  # empty
        #             break
        #         distance = i - index[-1] - 1
        #         res += (min(height[i], height[index[-1]]) - height[top]) * distance  # top < height[i] and top < height[index[-1]]
        #     index.append(i)  # until smaller than prev, then append
        # return res
    
        ## two pointer 1
        # left, right = 0, len(height)-1
        # leftMax, rightMax = 0, 0
        # res = 0
        # while left < right:
        #     if height[left] > leftMax:
        #         leftMax = height[left]
        #     if height[right] > rightMax:
        #         rightMax = height[right]
        #     if leftMax < rightMax:  # more intuitive if compare leftMax and rightMax
        #         res += (leftMax - height[left])
        #         left += 1
        #     else:
        #         res += (rightMax - height[right])
        #         right -= 1
        # return res
    
        ## two point 2
        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0
        res = 0
        while left < right:
            if height[left] < height[right]:  # it is sure that leftMax >= height[left], rightMax >= height[right] > height[left]
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    res += (leftMax - height[left])
                left += 1
            else:  # we use this to make sure rightMax >= leftMax?
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    res += (rightMax - height[right])
                right -= 1
        return res
                
