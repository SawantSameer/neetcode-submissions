class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        second_num = dict()
        for i in range(len(nums)):
            if target-nums[i] in second_num:
                return [second_num[target-nums[i]],i]
            second_num[nums[i]]=i