def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    edges = []
    
    for _ in range(M):
        a, b, d = map(int, input().split())
        edges.append((d, a, b))
    
    # 크루스칼 알고리즘
    edges.sort()
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    total_distance = 0
    edges_used = 0
    
    for d, a, b in edges:
        if union(parent, rank, a, b):
            total_distance += d
            edges_used += 1
            if edges_used == N - 1:
                break
    
    print(f"Case #{case}: {total_distance} meters")