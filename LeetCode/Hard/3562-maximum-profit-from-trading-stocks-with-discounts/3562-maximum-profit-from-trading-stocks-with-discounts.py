class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        children = [[] for _ in range(n)]
        for parent, child in hierarchy:
            children[parent - 1].append(child - 1)

        dp_table = [[[0] * (budget + 1) for _ in range(2)] for _ in range(n)]
        NEG_INF = -10**9

        def combine_arrays(a, b):
            result = [NEG_INF] * (budget + 1)
            for cost_a in range(budget + 1):
                val_a = a[cost_a]
                if val_a < 0:
                    continue
                max_b = budget - cost_a
                for cost_b in range(max_b + 1):
                    val_b = b[cost_b]
                    if val_b < 0:
                        continue
                    tot = cost_a + cost_b
                    cand = val_a + val_b
                    if cand > result[tot]:
                        result[tot] = cand
            return result

        def traverse(node):
            for ch in children[node]:
                traverse(ch)

            for parent_bought in (0, 1):
                price = present[node] // 2 if parent_bought else present[node]
                profit = future[node] - price

                skip_option = [0] * (budget + 1)
                for ch in children[node]:
                    skip_option = combine_arrays(skip_option, dp_table[ch][0])

                take_option = [NEG_INF] * (budget + 1)
                if price <= budget:
                    base_with_children = [0] * (budget + 1)
                    for ch in children[node]:
                        base_with_children = combine_arrays(base_with_children, dp_table[ch][1])
                    for total_cost in range(price, budget + 1):
                        prev = base_with_children[total_cost - price]
                        if prev > NEG_INF:
                            take_option[total_cost] = prev + profit

                for c in range(budget + 1):
                    dp_table[node][parent_bought][c] = skip_option[c] if skip_option[c] >= take_option[c] else take_option[c]

        traverse(0)
        return max(dp_table[0][0])