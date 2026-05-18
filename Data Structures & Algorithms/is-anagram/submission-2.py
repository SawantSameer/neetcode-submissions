class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit: lengths must match
        if len(s) != len(t):
            return False
            
        fr = dict()
        for char in s:
            fr[char] = 1 + fr.get(char, 0)
        
        for char in t:
            # If the char isn't there, OR if we've already used up all 
            # available counts of this char, it's not an anagram.
            if char not in fr or fr[char] == 0:
                return False
            fr[char] -= 1

        # We no longer need the third loop!
        return True