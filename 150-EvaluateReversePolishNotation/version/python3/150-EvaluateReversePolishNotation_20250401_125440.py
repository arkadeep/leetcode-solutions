# Last updated: 4/1/2025, 12:54:40 PM
# Managed to get O(n). Uses the operator package.
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        op_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for elem in tokens:
            if elem not in op_map:
                stack.append(int(elem))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(op_map[elem](val2, val1)))

        return stack[-1]
