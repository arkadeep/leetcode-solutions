# Last updated: 4/1/2025, 4:21:21 PM
# Needed help to solve. Need to revise.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Idea is to maintain a monotonic decreasing stack
        # adding elements if they are small
        # popping elements if they are larger

        # array holding the results - setting with 0 helps with default
        # values 
        res = [0] * len(temperatures)   
        # Contains a pair of values (temp, index)
        stack = []      


        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            
            stack.append([t, i])
        
        return res