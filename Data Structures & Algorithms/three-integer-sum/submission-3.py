class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        fr = {}
        for num in nums:
            fr[num] = 1 + fr.get(num, 0)    

        res = []        
        for i in range(len(nums)):
            fr[nums[i]]-=1
            if i and nums[i]==nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                fr[nums[j]] -=1
                if j-1 > i and nums[j]==nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                if target in fr and fr[target]>0:
                    res.append([nums[i], nums[j], target])
            for j in range(i+1, len(nums)):
                fr[nums[j]]+=1
        return res