class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        l,r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[r]<nums[m]:
                l = m+1
            else:
                r = m
        pivot = l
        
        def BS(l,r):
            while l<=r:
                m = (l+r)//2
                if nums[m]>target:
                    r = m - 1
                elif nums[m]<target:
                    l = m+1
                else:
                    return m
            return -1

        result = BS(0,pivot-1)
        if result!= -1:
            return result
        return BS(pivot, len(nums) - 1)