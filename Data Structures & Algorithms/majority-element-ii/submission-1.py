class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = len(nums)//3
        fr = dict()
        res = []
        for x in nums:
            fr[x] = 1 + fr.get(x, 0)

        for x in fr.keys():
            if fr[x]>t:
                res.append(x)

        return res