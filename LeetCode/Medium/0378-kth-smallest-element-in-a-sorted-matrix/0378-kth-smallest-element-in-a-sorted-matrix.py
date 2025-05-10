class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # 최소 힙 초기화: 각 행의 첫 번째 원소를 삽입
        min_heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(min_heap)
        
        # k번째 원소를 찾기 위해 힙에서 원소를 꺼냄
        for _ in range(k - 1):
            val, row, col = heapq.heappop(min_heap)
            # 다음 열의 원소를 힙에 삽입
            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
        
        # k번째 원소 반환
        return heapq.heappop(min_heap)[0]