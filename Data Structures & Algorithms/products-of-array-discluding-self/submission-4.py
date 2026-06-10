class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod(arr):
            product = 1
            for x in arr:
                product *= x
            return product
        
        n = len(nums)
        prefix,suffix = [1]*n,[prod(nums[1:])]*n

        for i in range(1,len(nums)):
            prefix[i] = prod(nums[0:i])
            suffix[i] = prod(nums[i+1:])

        res = [0]*n

        for i in range(n):
            res[i] = prefix[i]*suffix[i]
        return res
        