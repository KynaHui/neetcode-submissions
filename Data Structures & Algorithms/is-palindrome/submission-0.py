class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r: 
            # if !s[l].isalnum(): -> not C lol
            # l < r -> all punctuations, eg ".,"
            while l < r and not s[l].isalnum(): # not if, skip multiple punctuations
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True