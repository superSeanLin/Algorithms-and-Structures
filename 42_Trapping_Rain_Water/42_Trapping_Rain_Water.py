class Solution:
    def trap(self, height: List[int]) -> int:
        ## intuition: find left max and right max to calculate
        
        ## use stack 
        # index = []  # store height index
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
    
        ## two pointer
        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0
        res = 0
        while left < right:
            if height[left] < height[right]:  # depends on smaller bar
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    res += leftMax - height[left]
                left += 1
            else:  # depends on smaller bar
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    res += rightMax - height[right]
                right -= 1
        return res
                
