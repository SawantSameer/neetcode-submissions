class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n,res = len(nums), nums[0]
        for i in range(n):
            sums = 0
            for j in range(i, n):
                sums += nums[j]
                res = max(res, sums)

        return res