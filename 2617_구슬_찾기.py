# 2617 구슬 찾기 제출한 정답
from collections import deque


def BFS(x, graph):
    global ans
    
    Q = deque([x])
    ch = [0 for _ in range(n + 1)]
    ch[x] = 1
    cnt = 0
    
    while Q:
        x = Q.popleft()
        
        for i in graph[x]:
            if not ch[i]:
                Q.append(i)
                ch[i] = 1
                cnt += 1
                
                if cnt > mid:
                    ans += 1
                    return
                
                Q.append(i)


n, m = map(int, input().split())
mid = n // 2

graph_1 = [list() for _ in range(n + 1)]
graph_2 = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph_1[a].append(b)
    graph_2[b].append(a)

ans = 0
for i in range(1, n + 1):
    BFS(i, graph_1)
    BFS(i, graph_2)

print(ans)