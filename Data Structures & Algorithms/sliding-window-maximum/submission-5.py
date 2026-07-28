class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def findMax(l):
            mx = l[0]
            for i in range(1,len(l)):
                if l[i]>mx:
                    mx = l[i]

            return mx

        res = []
        for i in range(len(nums)-k+1):
            res.append(findMax(nums[i:i+k]))

        return res
