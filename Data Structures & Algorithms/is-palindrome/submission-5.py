class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for char in s:
            if char.isalnum():
                t = t+ char

        return t.lower()==t[::-1].lower()