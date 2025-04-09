# Last updated: 4/8/2025, 11:45:18 PM
# Needed help from neetcode
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