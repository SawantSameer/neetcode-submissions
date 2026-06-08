class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        if len(s1)==len(s2):
            return "".join(sorted(s1))== "".join(sorted(s2[0:len(s1)]))

        for i in range(len(s2)):
            if s2[i] in s1:
                if "".join(sorted(s1))=="".join(sorted(s2[i:i+len(s1)])):
                    return True
        
        return False
                    