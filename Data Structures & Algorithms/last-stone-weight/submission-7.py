import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap)>1:
            lar = heapq.heappop(heap)
            slar = heapq.heappop(heap)
            if slar>lar:
                heapq.heappush(heap, lar-slar)

        return -heap[0] if heap else 0
            