import heapq
import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input().rstrip())
for case_num in range(1, T + 1):
    N = int(input().rstrip())
    colors = list()
    color_to_rooms = defaultdict(list)
    for i in range(N):
        color = input().rstrip()
        colors.append(color)
        color_to_rooms[color].append(i)

    M = int(input().rstrip())
    edges = [list() for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().rstrip().split())
        edges[a - 1].append((b - 1, t))

    for room_list in color_to_rooms.values():
        if len(room_list) > 1:
            for i in room_list:
                for j in room_list:
                    if i != j:
                        edges[i].append((j, 0))

    S = int(input().rstrip())
    queries = list()
    for _ in range(S):
        p, q = map(int, input().rstrip().split())
        queries.append((p - 1, q - 1))

    print(f"Case #{case_num}:")
    for start, end in queries:
        dist = [float('inf')] * N
        dist[start] = 0
        hq = [(0, start)]
        visited = [False] * N
        while hq:
            cur_dist, u = heapq.heappop(hq)
            if visited[u]:
                continue
            visited[u] = True
            if u == end:
                break
            for v, w in edges[u]:
                if not visited[v] and dist[v] > cur_dist + w:
                    dist[v] = cur_dist + w
                    heapq.heappush(hq, (dist[v], v))
        print(dist[end] if dist[end] != float('inf') else -1)