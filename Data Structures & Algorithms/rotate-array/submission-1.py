class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = nums[-1::-1]
        n = len(nums)
        nums.reverse()
        # nums[:k] = nums[k-1::-1]
        if k>n:
            k = k%n
        s,e = 0,k-1
        while s<e:
            nums[s],nums[e] = nums[e],nums[s]
            s+=1
            e-=1
        #nums[k:] = nums[:k+1:-1]
        s,e = k,n-1
        while s<e:
            nums[s],nums[e] = nums[e],nums[s]
            s+=1
            e-=1

