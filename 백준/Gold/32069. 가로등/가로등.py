from collections import deque
import sys
input = sys.stdin.readline

L, N, K = map(int, input().rstrip().split())
lamp_positions = list(map(int, input().rstrip().split()))

Q = deque()
visited = set()
for pos in lamp_positions:
    if pos not in visited:
        visited.add(pos)
        Q.append((pos, 0))

ans = list()
while Q and len(ans) < K:
    pos, dark = Q.popleft()
    ans.append(dark)
    for delta in (-1, 1):
        npos = pos + delta
        if 0 <= npos <= L and npos not in visited:
            visited.add(npos)
            Q.append((npos, dark + 1))

for d in ans:
    print(d)