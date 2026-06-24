class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f = 0
        res = ''
        while f<len(word1) and f<len(word2):
            res+=word1[f]+word2[f]
            f+=1
        res+=word1[f:]
        res+=word2[f:]
        return res