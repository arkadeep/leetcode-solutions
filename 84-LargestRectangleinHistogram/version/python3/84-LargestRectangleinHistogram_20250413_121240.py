# Last updated: 4/13/2025, 12:12:40 PM
# The key thing here is to use a stack which stores the index as well as the height of each element. Then as we scan through the elements, we pop if the element has a height smaller than the preceding element in the stack. Furthermore, when something has been popped, the new element being pushed into the stack will have the index of the earliest popped elelemnt.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # If there are things left in the stack, then it means
        # we can extend them till the very end

        max_area = 0

        stack = [] # pair for index and height

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # this condition means that we will need to:
                # pop the element
                # calculate height
                # extend current height backwards
                index, height = stack.pop()

                max_area = max(max_area, height * (i - index))

                start = index
            
            stack.append((start, h))
        
        # for remnants in the stack, we need to calculate the height
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area