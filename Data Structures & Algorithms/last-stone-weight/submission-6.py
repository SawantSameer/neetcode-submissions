import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mHeap = [-x for x in stones]
        heapq.heapify(mHeap)
    
     # I need to do the following operations:
     #Every iteration requires exactly this:

        # Remove the largest stone.
        # Remove the second largest stone.
        # If they're different, insert their difference.
        
        while len(mHeap)>1:
            lar = heapq.heappop(mHeap)
            slar = heapq.heappop(mHeap)
            if slar > lar:
                heapq.heappush(mHeap, lar-slar)

        return -mHeap[0] if mHeap else 0
            