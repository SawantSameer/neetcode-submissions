class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        def BS(l, r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l = mid+1
                else: r= mid-1

            return -1

        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[r]<nums[m]:
                l = m+1
            else:
                r = m

        pivot = l

        # result = BS(0, pivot-1)
        # if result!=-1:
        #     return result

        # return BS(pivot, len(nums)-1)

        if target > nums[-1]:
            return BS(0, pivot-1)
        return BS(pivot, len(nums)-1)
        
