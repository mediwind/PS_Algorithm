import sys
import heapq
input = sys.stdin.readline

T = int(input().rstrip())
for case in range(1, T + 1):
    N = int(input().rstrip())
    colors = [input().rstrip() for _ in range(N)]

    color_id = {}
    adj = []
    total = N
    for i in range(N):
        c = colors[i]
        if c not in color_id:
            color_id[c] = total
            total += 1
            adj.append([])
        adj.append([])

    adj = [[] for _ in range(total)]
    for i in range(N):
        cid = color_id[colors[i]]
        adj[i].append((cid, 0))
        adj[cid].append((i, 0))

    M = int(input())
    for _ in range(M):
        a, b, t = map(int, input().split())
        adj[a - 1].append((b - 1, t))

    S = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(S)]

    dist_cache = {}

    def dijkstra(src):
        dist = [float('inf')] * total
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        return dist

    print(f"Case #{case}:")
    for start, end in queries:
        start -= 1
        end -= 1
        if start not in dist_cache:
            dist_cache[start] = dijkstra(start)
        ans = dist_cache[start][end]
        print(-1 if ans == float('inf') else ans)