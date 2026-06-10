class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        fr = {}
        for x in nums:
            fr[x] = 1 + fr.get(x,0)

        most_freq = dict(sorted(fr.items(),key = lambda item:item[1],reverse=True))

        res = []
        for item in most_freq:
            if k==0:
                break
            res.append(item)
            k-=1
        return res