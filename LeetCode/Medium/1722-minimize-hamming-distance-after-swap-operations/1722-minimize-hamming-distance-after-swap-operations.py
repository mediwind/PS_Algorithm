class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        from typing import List
        from collections import defaultdict, Counter        

        # --- Union-Find ---
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        
        # 연결
        for u, v in allowedSwaps:
            union(u, v)
        
        # --- 그룹 만들기 ---
        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)
        
        # --- 각 그룹에서 mismatch 계산 ---
        mismatch = 0
        
        for indices in groups.values():
            count = Counter()
            
            # source 카운트
            for i in indices:
                count[source[i]] += 1
            
            # target으로 매칭
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    mismatch += 1
        
        return mismatch