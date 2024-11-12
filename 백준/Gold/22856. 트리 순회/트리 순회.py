import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def edge_count(x):
    global cnt
    ch[x] = True
    
    if not ch[graph[x][0]] and graph[x][0] != -1:
        edge_count(graph[x][0])
        cnt += 1
    if not ch[graph[x][1]] and graph[x][1] != -1:
        edge_count(graph[x][1])
        cnt += 1


def right_oneway_count(x):
    global cnt
    ch[x] = True
    
    if not ch[graph[x][1]] and graph[x][1] != -1:
        right_oneway_count(graph[x][1])
        cnt += 1


n = int(input())
graph = [list() for _ in range(n + 1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a] = [b, c]

ch = [0 for _ in range(n + 1)]
cnt = 0
edge_count(1)
ans = cnt

ch = [0 for _ in range(n + 1)]
cnt = 0
right_oneway_count(1)
ans = 2 * ans - cnt
print(ans)