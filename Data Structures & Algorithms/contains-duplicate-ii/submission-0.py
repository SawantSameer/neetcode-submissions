class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        fr = {}
        
        for i in range(len(nums)):
            if nums[i] in fr and i - fr[nums[i]]<=k:
                return True
            fr[nums[i]] = i

        return False
            
