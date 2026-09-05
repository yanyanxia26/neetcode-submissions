class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1 
        trap = 0
        maxleft = height[l]
        maxright = height[r]

        while l < r:
            if maxleft < maxright:
                l += 1
                maxleft = max(maxleft, height[l])
                trap += maxleft - height[l]
            else:
                r -= 1
                maxright = max(maxright, height[r])
                trap += maxright - height[r]
        
        return trap
