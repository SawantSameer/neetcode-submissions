class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = globalMax = nums[0]

        for num in nums[1:]:
            curMax = max(curMax+num, num)
            if curMax>globalMax:
                globalMax=curMax

        return globalMax