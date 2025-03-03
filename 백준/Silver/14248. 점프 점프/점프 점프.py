from collections import deque

n = int(input())
stones = list(map(int, input().split()))
start = int(input())
start -= 1

ch = [0 for _ in range(n)]
ch[start] = 1

Q = deque()
Q.append((start, stones[start]))
while Q:
    idx, x = Q.popleft()
    forward = idx + x
    backward = idx - x

    if 0 <= forward < n and not ch[forward]:
        ch[forward] = 1
        Q.append((forward, stones[forward]))

    if 0 <= backward < n and not ch[backward]:
        ch[backward] = 1
        Q.append((backward, stones[backward]))

print(sum(ch))