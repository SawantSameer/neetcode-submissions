class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,1
        n = len(set(nums))
        while r<n:
            if nums[r]==nums[l]:
                nums.append(nums.pop(r))
            else:
                l+=1
                r+=1
        return n