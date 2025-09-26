class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq

        heap = [-p for p in piles]
        heapq.heapify(heap)

        for _ in range(k):
            x = -heapq.heappop(heap)
            x -= x // 2
            heapq.heappush(heap, -x)
            
        return -sum(heap)