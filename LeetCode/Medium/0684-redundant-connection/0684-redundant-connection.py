class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        def find(x):
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        

        def union(a, b):
            pa, pb = find(a), find(b)

            if pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb
        

        parent = list(range(max(map(max, edges)) + 1))

        for a, b in edges:
            pa, pb = find(a), find(b)

            if pa == pb:
                return [a, b]
                
            union(pa, pb)
                
