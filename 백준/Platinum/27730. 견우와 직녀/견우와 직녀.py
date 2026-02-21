import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline


def get_min_dist_node(n, edges):
    if n == 1:
        return 1, 0
        
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    subtree_size = [0] * (n + 1)
    subtree_dist = [0] * (n + 1)

    
    def dfs1(curr, parent):
        subtree_size[curr] = 1
        for nxt, weight in adj[curr]:
            if nxt != parent:
                dfs1(nxt, curr)
                subtree_size[curr] += subtree_size[nxt]
                subtree_dist[curr] += subtree_dist[nxt] + subtree_size[nxt] * weight
                
    dfs1(1, 0)
    
    total_dist = [0] * (n + 1)
    total_dist[1] = subtree_dist[1]

    
    def dfs2(curr, parent):
        for nxt, weight in adj[curr]:
            if nxt != parent:
                total_dist[nxt] = total_dist[curr] - subtree_size[nxt] * weight + (n - subtree_size[nxt]) * weight
                dfs2(nxt, curr)
                
    dfs2(1, 0)
    
    min_dist = float('inf')
    best_node = -1
    
    for i in range(1, n + 1):
        if total_dist[i] < min_dist:
            min_dist = total_dist[i]
            best_node = i
            
    return best_node, min_dist


n_str = input().strip()
if n_str:
    N = int(n_str)
    edges_E = []
    for _ in range(N - 1):
        u, v, c = map(int, input().split())
        edges_E.append((u, v, c))
        
    M = int(input().strip())
    edges_W = []
    for _ in range(M - 1):
        u, v, c = map(int, input().split())
        edges_W.append((u, v, c))
        
    u_opt, min_E = get_min_dist_node(N, edges_E)
    v_opt, min_W = get_min_dist_node(M, edges_W)

    total_sum = M * min_E + N * M + N * min_W

    print(f"{u_opt} {v_opt}")
    print(total_sum)