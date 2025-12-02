class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        from typing import List, Dict
        
        MOD = 10**9 + 7
        groups: Dict[int, int] = defaultdict(int)
        for _, y in points:
            groups[y] += 1

        result = 0
        total_pairs = 0
        for count in groups.values():
            pairs = count * (count - 1) // 2
            result = (result + total_pairs * pairs) % MOD
            total_pairs = (total_pairs + pairs) % MOD

        return result