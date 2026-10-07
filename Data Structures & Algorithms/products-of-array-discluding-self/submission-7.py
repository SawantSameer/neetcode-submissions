class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numOfZeros = 0
        for num in nums:
            if not num:
                numOfZeros+=1
        res = []
        if numOfZeros == 0:
            prod = 1
            for num in nums:
                prod*=num
            for num in nums:
                res.append(int(prod/num))

        elif numOfZeros==1:
            prod = 1
            for num in nums:
                if num:
                    prod*=num
            for num in nums:
                if not num:
                    res.append(prod)
                else:
                    res.append(0)

        else:
            res = [0 for _ in range(len(nums))]

        return res