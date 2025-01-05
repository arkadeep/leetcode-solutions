class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # pointer1 = 0

        # pointer2 = len(s) - 1

        # removing non alphanumeric character
        s = (''.join(ch for ch in s if ch.isalnum()))

        # converting to lowercase
        s = s.lower()

        if s == s[::-1]:
            return True
        else:
            return False