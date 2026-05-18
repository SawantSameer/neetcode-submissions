class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fr = dict()
        for char in s:
            fr[char] = 1+ fr.get(char,0)
        
        for char in t:
            if char not in fr:
                return False
            fr[char]-=1

        for items in fr:
            if fr[items]!=0:
                return False

        return True