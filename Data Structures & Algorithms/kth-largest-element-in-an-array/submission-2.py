import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-x for x in nums]
        heapq.heapify(minHeap)

        while k!=1:
            k-=1
            heapq.heappop(minHeap)
        return -heapq.heappop(minHeap)