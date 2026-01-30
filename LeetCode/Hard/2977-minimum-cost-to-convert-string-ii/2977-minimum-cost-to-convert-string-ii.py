class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        infinity = 10**30
        string_to_index = {}
        valid_lengths = set()
        node_count = 0

        distance = [[infinity] * 201 for _ in range(201)]

        for src, dst, price in zip(original, changed, cost):
            if src not in string_to_index:
                string_to_index[src] = node_count
                valid_lengths.add(len(src))
                node_count += 1
            if dst not in string_to_index:
                string_to_index[dst] = node_count
                node_count += 1
            src_idx = string_to_index[src]
            dst_idx = string_to_index[dst]
            distance[src_idx][dst_idx] = min(distance[src_idx][dst_idx], price)

        for idx in range(node_count):
            distance[idx][idx] = 0

        for mid in range(node_count):
            for start in range(node_count):
                if distance[start][mid] < infinity:
                    for end in range(node_count):
                        if distance[mid][end] < infinity:
                            distance[start][end] = min(
                                distance[start][end],
                                distance[start][mid] + distance[mid][end],
                            )

        length = len(source)
        dp_cost = [infinity] * (length + 1)
        dp_cost[0] = 0

        for pos in range(length):
            if dp_cost[pos] == infinity:
                continue

            if source[pos] == target[pos]:
                dp_cost[pos + 1] = min(dp_cost[pos + 1], dp_cost[pos])

            for seg_len in valid_lengths:
                if pos + seg_len > length:
                    continue
                src_seg = source[pos : pos + seg_len]
                dst_seg = target[pos : pos + seg_len]
                if src_seg in string_to_index and dst_seg in string_to_index:
                    dp_cost[pos + seg_len] = min(
                        dp_cost[pos + seg_len],
                        dp_cost[pos]
                        + distance[
                            string_to_index[src_seg]
                        ][
                            string_to_index[dst_seg]
                        ],
                    )

        return -1 if dp_cost[length] == infinity else dp_cost[length]