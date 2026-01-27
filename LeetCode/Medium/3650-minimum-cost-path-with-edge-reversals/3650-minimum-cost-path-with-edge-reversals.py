class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = [[] for _ in range(n)]
        for start, end, weight in edges:
            adjacency_list[start].append((weight, end))
            adjacency_list[end].append((weight << 1, start))

        distances = [0] + [inf] * (n - 1)
        priority_queue = [(0, 0)]
        heapq.heapify(priority_queue)

        while priority_queue:
            current_dist, node = heapq.heappop(priority_queue)

            if current_dist > distances[node]:
                continue
            if node == n - 1:
                return current_dist

            for edge_weight, next_node in adjacency_list[node]:
                new_dist = current_dist + edge_weight
                if new_dist < distances[next_node]:
                    distances[next_node] = new_dist
                    heapq.heappush(priority_queue, (new_dist, next_node))

        return -1