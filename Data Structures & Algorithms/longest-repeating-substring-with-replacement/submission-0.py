class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # n = len(s)
        # charList = dict()
        # for i,char in enumerate(s):
        #     if char in charList:
        #         charList[char].append(i)
        #     else:
        #         charList[char] = [i]
        # print(charList)
        
        res = 0
        for i in range(len(s)):
            fr,maxf = dict(), 0
            for j in range(i,len(s)):
                # if s[j] in fr:
                #     fr[s[j]]+=1
                # else:
                #     fr[s[j]]=1

                fr[s[j]]= 1+ fr.get(s[j],0)
                maxf = max(maxf, fr[s[j]])
                if (j-i+1)-maxf <= k:
                    res = max(res, j-i+1)

        return res
            
