class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1

        result = 0

        while left < right:

            area = min(height[left], height[right]) * (right - left)
            result = max(area, result)

            if height[right] < height[left] or height[right] == height[left]:
                right -= 1
            else:
                left += 1

        return result





