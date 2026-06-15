class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        
        heapq.heapify(nums)
        
        k_largest = heapq.nsmallest(k,nums)
        return (-k_largest[-1])
