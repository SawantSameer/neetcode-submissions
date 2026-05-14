from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        
        def mostCount(d : dict):
            for x in d:
                if d[x]==max(d.values()):
                    return x 
        ans = []
        while k!=0:
            ans.append(mostCount(freq))
            freq.pop(mostCount(freq))
            k-=1
        return ans
