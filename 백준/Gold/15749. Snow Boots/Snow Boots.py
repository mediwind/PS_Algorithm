from collections import deque
import sys
input = sys.stdin.readline

N, B = map(int, input().rstrip().split())
f = list(map(int, input().rstrip().split()))
boots = [tuple(map(int, input().rstrip().split())) for _ in range(B)]

# visited[pos][boot_idx]: 해당 위치에서 해당 부츠로 방문했는지
visited = [[False] * B for _ in range(N)]
queue = deque()
queue.append((0, 0))  # (현재 위치, 현재 부츠 인덱스)
visited[0][0] = True

while queue:
    pos, boot = queue.popleft()
    s, d = boots[boot]
    # 앞으로 이동
    for step in range(1, d + 1):
        next_pos = pos + step
        if next_pos < N and f[next_pos] <= s and not visited[next_pos][boot]:
            visited[next_pos][boot] = True
            queue.append((next_pos, boot))
    # 부츠 교환
    for next_boot in range(boot + 1, B):
        if f[pos] <= boots[next_boot][0] and not visited[pos][next_boot]:
            visited[pos][next_boot] = True
            queue.append((pos, next_boot))

# 도착지에 도달한 최소 부츠 인덱스(버린 횟수)
for boot in range(B):
    if visited[N - 1][boot]:
        print(boot)
        break