class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        import heapq
        
        parent = list(range(c+1))
        rank = [0]*(c+1)

        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x

        def union(a,b):
            ra,rb=find(a),find(b)
            if ra==rb: return
            if rank[ra]<rank[rb]:
                parent[ra]=rb
            else:
                parent[rb]=ra
                if rank[ra]==rank[rb]:
                    rank[ra]+=1

        for u,v in connections:
            union(u,v)

        comp = [0]*(c+1)
        for i in range(1,c+1):
            comp[i]=find(i)

        heaps = defaultdict(list)
        for i in range(1,c+1):
            heaps[comp[i]].append(i)
        for k in heaps:
            heapq.heapify(heaps[k])

        online = [True]*(c+1)
        res = []
        for typ,x in queries:
            if typ==2:
                online[x]=False
            else:
                if online[x]:
                    res.append(x)
                else:
                    h = heaps[comp[x]]
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    if not h:
                        res.append(-1)
                    else:
                        res.append(h[0])
                        
        return res