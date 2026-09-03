class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_aera = 0

        while left < right:
            length = right - left
            height = min(heights[right], heights[left])
            aera = length * height
            
            max_aera = max(max_aera, aera)

            if heights[right] < heights[left]:
                right -= 1

            else:
                left += 1
        return max_aera

            



            

        