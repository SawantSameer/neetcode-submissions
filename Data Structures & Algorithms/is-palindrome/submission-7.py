class Solution:
    def isPalindrome(self, s: str) -> bool:
        ms = ""

        for char in s:
            if char.isalnum():
                ms += char.lower()

        l,r = 0, len(ms)-1
        while l<r:
            if ms[l]!=ms[r]:
                return False
            l+=1
            r-=1
        return True