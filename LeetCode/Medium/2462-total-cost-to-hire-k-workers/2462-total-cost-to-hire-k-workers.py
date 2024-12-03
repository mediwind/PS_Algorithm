class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        head = list()
        tail = list()

        head_idx = 0
        tail_idx = n - 1

        answer = 0
        for _ in range(k):
            while len(head) < candidates and head_idx <= tail_idx:
                heapq.heappush(head, costs[head_idx])
                head_idx += 1
            while len(tail) < candidates and head_idx <= tail_idx:
                heapq.heappush(tail, costs[tail_idx])
                tail_idx -= 1
            
            c1, c2 = float("inf"), float("inf")
            if head:
                c1 = head[0]
            if tail:
                c2 = tail[0]
            
            if c1 <= c2:
                answer += c1
                heapq.heappop(head)
            else:
                answer += c2
                heapq.heappop(tail)
        
        return answer