class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        from typing import List, Set

        adj = defaultdict(list)
        src = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        component_count = 0
        visited_nodes: Set[int] = set()

        def dfs(node: int) -> int:
            nonlocal component_count
            if node in visited_nodes:
                return 0
            visited_nodes.add(node)
            subtotal = values[node]
            for neighbor in adj[node]:
                subtotal += dfs(neighbor)
            if subtotal % k == 0:
                component_count += 1
                return 0
            return subtotal % k

        dfs(src)
        
        return component_count