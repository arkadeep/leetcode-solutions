from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # This solution is O(m*n)
        # More efficient O(n) solution is possible

        left = 0

        s1_dict = Counter(s1)

        for right in range(len(s2)):

            if (right - left + 1) < len(s1):
                print("The pointers have a string smaller than s1")
                print("Continuing")
                continue
            elif (right - left + 1) > len(s1):
                print("This is the case where the pointer string is longer")
                print("Incrementing the left pointer")
                left += 1
            else:
                print("this is the case where the pointer string is the same length")
                pointer_dict = Counter(s2[left: right+1])
                if pointer_dict == s1_dict:
                    return True
                else:
                    left += 1
            
        return False
