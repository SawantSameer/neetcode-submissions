class Solution:
    def firstUniqChar(self, s: str) -> int:
        fr = {}
        for char in s:
            fr[char] = fr.get(char, 0)+1

        for i, char in enumerate(s):
            if fr[char]==1:
                return i
        return -1
