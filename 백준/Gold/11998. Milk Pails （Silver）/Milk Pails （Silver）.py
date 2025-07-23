from collections import deque

X, Y, K, M = map(int, input().split())

ch = [[0 for _ in range(Y + 1)] for _ in range(X + 1)]
Q = deque()
Q.append((0, 0, 0)) # x, y, step
ch[0][0] = 1

ans = float('inf')
while Q:
    x, y, step = Q.popleft()
    ans = min(ans, abs(x + y - M))
    if step == K:
        continue
    
    next_states = [
        (X, y), # X를 채움
        (x, Y), # Y를 채움
        (0, y), # X를 비움
        (x, 0), # Y를 비움
        # X에서 Y로 붓기
        (x - min(x, Y - y), y + min(x, Y - y)),
        (x + min(y, X - x), y - min(y, X - x))
    ]
    
    for nx, ny in next_states:
        if not ch[nx][ny]:
            ch[nx][ny] = 1
            Q.append((nx, ny, step + 1))

print(ans)