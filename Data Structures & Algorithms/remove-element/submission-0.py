class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for x in nums:
            if x==val:count+=1
        i = 0
        while i<len(nums)-count:
            if nums[i]==val:
                nums.append(nums.pop(i))
            else:
                i+=1
        return len(nums)-count