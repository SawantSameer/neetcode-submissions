class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n==1:
            return nums

        fr= {}
        for num in nums:
            fr[num] = 1 + fr.get(num,0)

        most_freq = dict(sorted(fr.items(), key=lambda item: item[1], reverse=True))
        
        res = []
        for item in most_freq:
            if k==0:
                break
            res.append(item)
            k-=1
        return res
