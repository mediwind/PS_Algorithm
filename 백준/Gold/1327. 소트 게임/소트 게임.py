from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = tuple(map(int, input().split()))
target = tuple(range(1, N+1))
if arr == target:
    print(0)
    sys.exit(0)

q = deque([arr])
dist = {arr: 0}

while q:
    cur = q.popleft()
    d = dist[cur]
    for i in range(0, N - K + 1):
        nxt = list(cur)
        nxt[i:i+K] = reversed(nxt[i:i+K])
        nxt = tuple(nxt)
        if nxt not in dist:
            if nxt == target:
                print(d + 1)
                sys.exit(0)
            dist[nxt] = d + 1
            q.append(nxt)

print(-1)