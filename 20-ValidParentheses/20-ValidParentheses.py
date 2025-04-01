# Last updated: 3/31/2025, 11:57:50 PM
class Solution:
    def isValid(self, s: str) -> bool:
        
        append_elems = "({["
        pop_elems = ")}]"

        pop_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        # What are the conditions?
            # Stack must be empty

        stack_len = 0
        for char in s:
            # print(char)
            if char in append_elems:
                # print(f"{char} is an append elem")
                stack.append(char)
                stack_len += 1
                # print(f"stack: {stack}")
            if char in pop_elems:
                # print(f"{char} is a pop elem")
                # print(stack[-1])
                if stack_len < 1:
                    return False
                if pop_dict.get(stack[-1]) == char:
                    stack.pop()
                    stack_len -= 1
                    # print(f"stack: {stack}")
                else:
                    return False
        
        # print(stack)
        if len(stack) == 0:
            return True
        else:
            return False


