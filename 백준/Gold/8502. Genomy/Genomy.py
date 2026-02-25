import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n, m = map(int, input().strip().split())

pos = [[0] * (n + 1) for _ in range(m)]

for i in range(m):
    seq = list(map(int, input().split()))
    for j in range(n):
        gene = seq[j]
        pos[i][gene] = j

adj = [[] for _ in range(n + 1)]

for u in range(1, n + 1):
    for v in range(1, n + 1):
        if u == v:
            continue
            
        always_before = True
        for i in range(m):
            if pos[i][u] > pos[i][v]:
                always_before = False
                break
                
        if always_before:
            adj[u].append(v)

dp = [-1] * (n + 1)

def get_longest(u):
    if dp[u] != -1:
        return dp[u]
        
    max_len = 0
    for v in adj[u]:
        max_len = max(max_len, get_longest(v))
        
    dp[u] = max_len + 1
    return dp[u]

ans = 0
for i in range(1, n + 1):
    ans = max(ans, get_longest(i))

print(ans)