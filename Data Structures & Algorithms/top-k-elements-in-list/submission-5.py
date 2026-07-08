class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fr = {}
        if len(nums)==1:
            return nums
        for num in nums:
            fr[num] = 1 + fr.get(num, 0)

        most_freq = dict(sorted(fr.items(), key=lambda item: item[1], reverse = True))

        res = list(most_freq.keys())[:k]
        return res