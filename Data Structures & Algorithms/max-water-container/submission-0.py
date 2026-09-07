class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            height = min(heights[left],heights[right])
            vol = height * (right - left)
            area = max(area,vol)

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        
        return area
