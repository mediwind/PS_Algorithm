from collections import deque
import sys
input = sys.stdin.readline


def BFS(start):
    Q = deque()
    Q.append(start)
    check.add(start)
    while Q:
        x = Q.popleft()
        nodes_of_now_depth = list()
        for node in graph[x]:
            if not node in check:
                check.add(node)
                nodes_of_now_depth.append(node)
        
        sub_arr = order[start:start + len(nodes_of_now_depth)]
        if sorted(nodes_of_now_depth) != sorted(sub_arr):
            return 0
        
        for i in sub_arr:
            Q.append(i)
        start += len(nodes_of_now_depth)
    
    return 1


n = int(input())
graph = [list() for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
order = list(map(int, input().split()))
check = set()
if order[0] != 1:
    print(0)
else:
    print(BFS(1))