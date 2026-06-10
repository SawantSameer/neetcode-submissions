class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        
        # 1. Build the prefix array by carrying the product forward
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        # 2. Build the suffix array by carrying the product backward
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
            
        # 3. Multiply them together
        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
            
        return res