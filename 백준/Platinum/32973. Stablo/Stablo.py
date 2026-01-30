import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(u, d):
    depth[u] = d
    current_sum = v[u]
    current_dist = 0

    for child in adj[u]:
        dfs(child, d + 1)
        current_sum += sub_sum[child]
        current_dist += sub_dist[child] + sub_sum[child]

    sub_sum[u] = current_sum
    sub_dist[u] = current_dist

def get_kth_ancestor(node, k):
    for j in range(LOG):
        if (k >> j) & 1:
            node = up[node][j]
    return node

N, Q = map(int, input().split())
v = [0] + list(map(int, input().split()))
parents_input = list(map(int, input().split()))

adj = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for i, p_node in enumerate(parents_input):
    child_node = i + 2
    adj[p_node].append(child_node)
    parent[child_node] = p_node

depth = [0] * (N + 1)
sub_sum = [0] * (N + 1)
sub_dist = [0] * (N + 1)

dfs(1, 0)

LOG = 20
up = [[0] * LOG for _ in range(N + 1)]

for i in range(1, N + 1):
    up[i][0] = parent[i]

for j in range(1, LOG):
    for i in range(1, N + 1):
        if up[i][j-1] != 0:
            up[i][j] = up[up[i][j-1]][j-1]

results = []
for _ in range(Q):
    x, y = map(int, input().split())

    if parent[x] == y:
        results.append(str(sub_dist[y]))
        continue

    dist_x_y = depth[x] - depth[y]
    z = get_kth_ancestor(x, dist_x_y - 1)
    
    delta = (sub_sum[z] - sub_sum[x]) + v[x] * (1 - dist_x_y)
    ans = sub_dist[y] + delta
    
    results.append(str(ans))

print("\n".join(results))