class Solution:
    def trap(self, height: List[int]) -> int:
        
        # two pointer approach

        if not height:
            return 0

        l, r = 0, len(height) - 1

        res = 0

        # starting position for the left max and right max
        left_max, right_max = height[l], height[r]

        while l < r:

            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res
