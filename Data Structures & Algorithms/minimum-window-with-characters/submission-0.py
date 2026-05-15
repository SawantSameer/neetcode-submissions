class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for char in t:
            countT[char]=  1+ countT.get(char,0)

        res = [-1,1]
        resLen = float("infinity")
        for i in range(len(s)):
            countS = {}
            for j in range(i,len(s)):
                # if s[j] in countT:
                #     countS[s[j]] = 1 + countS.get(s[j],0)
                countS[s[j]]=1+countS.get(s[j],0)
                
                #checking if the current substring from i to j contains t in init 
                # i.e, for each char c in countT, countS[c] is at least countT[c]
                flag = True
                for c in countT:
                    if countS.get(c,0)<countT[c]:
                        flag = False
                        break
                
                if flag and (j-i+1)<resLen:
                    resLen = j-i+1
                    res = [i,j]
        l,r= res
        return s[l: r+1] if resLen != float("infinity") else ""
                     