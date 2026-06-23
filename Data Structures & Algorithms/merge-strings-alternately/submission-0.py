class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f = 0
        res = ''
        while f<len(word1) and f<len(word2):
            res+=word1[f]+word2[f]
            f+=1
        if f==len(word1) or f==len(word2):
            if f<len(word1):
                res+=word1[f:]
            if f<len(word2):
                res+=word2[f:]
        return res