class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        res = 0
        l,r = 0,0
        def maxCounting(count):
            maxValue = 0
            for x in count.keys():
                if count[x]>=maxValue:
                    maxValue = count[x]

            return maxValue
        while r<len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxCount = maxCounting(count)
            if (r-l+1)-maxCount <= k:
                res = max(res, r-l+1)
                r+=1
            else:
                count[s[l]]-=1
                l+=1
                r+=1

        
        return res