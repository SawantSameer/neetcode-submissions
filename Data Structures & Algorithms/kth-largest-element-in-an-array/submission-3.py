import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-x for x in nums]
        heapq.heapify(minHeap)

        k_largest = heapq.nsmallest(k, minHeap)
        return (-k_largest[-1])