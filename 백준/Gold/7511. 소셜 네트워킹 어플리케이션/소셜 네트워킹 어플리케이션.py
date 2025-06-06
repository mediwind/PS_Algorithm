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


T = int(input().rstrip())
for t in range(1, T + 1):
    N = int(input().rstrip())
    parents = list(range(N))
    
    K = int(input().rstrip())
    for _ in range(K):
        a, b = map(int, input().rstrip().split())
        union(a, b)
    
    for i in range(N):
        find(i)
    
    M = int(input().rstrip())
    res = list()
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        
        if parents[a] == parents[b]:
            res.append(1)
        else:
            res.append(0)
    
    print(f"Scenario {t}:")
    for ans in res:
        print(ans)
    print()