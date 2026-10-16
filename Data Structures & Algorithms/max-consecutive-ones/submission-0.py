class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i,j = 0,1
        maxCount = 0

        while i<len(nums):
            count = 0
            if nums[i]:
                count +=1
                j = i+1
                while j<len(nums):
                    if nums[j]:
                        count+=1
                    else:
                        break
                    j+=1
                maxCount = max(maxCount, count)
                i = j
            else:
                count = 0
                i+=1
        return maxCount
