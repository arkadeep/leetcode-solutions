class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()

        # Sliding window technique required
        # a left pointer will start at 0 and then the right pointer is the loop

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res