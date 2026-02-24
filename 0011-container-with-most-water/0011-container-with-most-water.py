class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        n = len(height)
        left,right = 0,n-1
        while left < right:
            maxArea = max(maxArea,min(height[left],height[right]) * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea