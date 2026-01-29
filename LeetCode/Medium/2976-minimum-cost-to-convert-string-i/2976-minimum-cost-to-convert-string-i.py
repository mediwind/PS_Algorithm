class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        distance = [[float("inf")] * 26 for _ in range(26)]

        for idx in range(26):
            distance[idx][idx] = 0

        for idx in range(len(original)):
            from_char = ord(original[idx]) - ord("a")
            to_char = ord(changed[idx]) - ord("a")
            distance[from_char][to_char] = min(
                distance[from_char][to_char], cost[idx]
            )

        for mid in range(26):
            for start in range(26):
                for end in range(26):
                    distance[start][end] = min(
                        distance[start][end],
                        distance[start][mid] + distance[mid][end],
                    )

        total_cost = 0
        for idx in range(len(source)):
            start_char = ord(source[idx]) - ord("a")
            end_char = ord(target[idx]) - ord("a")

            if start_char == end_char:
                continue

            if distance[start_char][end_char] == float("inf"):
                return -1

            total_cost += distance[start_char][end_char]

        return total_cost