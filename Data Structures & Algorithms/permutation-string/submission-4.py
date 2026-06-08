class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        if len(s1)==len(s2):
            return "".join(sorted(s1))== "".join(sorted(s2[0:len(s1)]))
        arranged = "".join(sorted(s1))
        l,r = 0,len(s1)-1
        while r<len(s2):
            if arranged == "".join(sorted(s2[l:r+1])):
                return True
            r+=1
            l+=1
        return False

                    