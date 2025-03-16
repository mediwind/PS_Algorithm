import sys
input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    pa, pb = find(a), find(b)
    
    if pa <= pb:
        parents[pb] = pa
    else:
        parents[pa] = pb


n, m = map(int, input().rstrip().split())
parents = list(range(n + 1))
graph = list()
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    
    if parents[a] == parents[b]:
        continue
    
    union(a, b)

for i in range(1, n + 1):
    parents[i] = find(i)

order = list(map(int, input().rstrip().split()))

ans = 0
for i in range(1, n):
    prev, now = order[i - 1], order[i]
    if parents[now] != parents[prev]:
        ans += 1

print(ans)