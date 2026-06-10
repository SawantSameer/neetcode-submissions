class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        product = 1
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
        res = [0]*n
        if zero_count>1:
            return [0 for i in range(n)]
        elif zero_count == 1:
            for i in range(n):
                if nums[i]==0:
                    res[i] = product
                else:
                    res[i]=0
        else:
            for i in range(n):
                res[i] = product//nums[i]

        return res