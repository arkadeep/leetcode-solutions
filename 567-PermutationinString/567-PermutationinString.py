from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s2 is shorter than s1, we wont find a solution
        if len(s2) < len(s1):
            return False

        left = 0

        s1_dict = Counter(s1)
        window_dict = Counter()

        for right in range(len(s2)):

            window_dict[s2[right]] += 1

            # If the len of the pointer string is smaller than s1, we keep adding
            if (right - left + 1) < len(s1):
                continue

            # If wondow is larger than s1, remove the left most character
            elif (right - left + 1) > len(s1):
                window_dict[s2[left]] -= 1
                # If the count is 0, then we remove the key
                if window_dict[s2[left]] == 0:
                    del window_dict[s2[left]]
                
                left += 1

            # if the window is the same size, check for permutation
            if window_dict == s1_dict:
                return True

        return False
