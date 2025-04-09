# Last updated: 4/9/2025, 12:36:05 AM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # print(pair)
        # print(sorted(pair))
        # print(sorted(pair)[::-1])

        for p, s in sorted(pair)[::-1]:      # reverse sorted order based on position
        # this makes sense since a faster car would have to overtake the slower car 
        # in front of it to be able to get to the target
            # print(p, s)

            stack.append((target - p) / s)
            # after appending, we need to check if it overlaps with the other element

            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # if the time is less than the one which is one below, then it means that they will collide
                stack.pop()

        return len(stack)