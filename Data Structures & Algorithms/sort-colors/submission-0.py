class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sorting(l):
            for i in range(len(l)-1):
                for j in range(len(l)-1-i):
                    if l[j]>l[j+1]:
                        l[j],l[j+1] = l[j+1], l[j]

        sorting(nums)