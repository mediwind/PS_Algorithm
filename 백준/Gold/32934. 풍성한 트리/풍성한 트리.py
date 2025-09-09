from collections import deque
import sys
# input = sys.stdin.readline

def bfs(start_node, n, graph):
    distances = [-1] * (n + 1)
    distances[start_node] = 0
    queue = deque([start_node])
    farthest_node = start_node

    while queue:
        curr = queue.popleft()
        if distances[curr] > distances[farthest_node]:
            farthest_node = curr
        
        for neighbor in graph[curr]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[curr] + 1
                queue.append(neighbor)
    
    return farthest_node, distances

def solve():
    N = int(input().rstrip())
    edges = [tuple(map(int, input().rstrip().split())) for _ in range(N - 1)]

    if N < 4 or (N + 2) % 3 != 0:
        print(-1)
        return
    
    power_of_2 = (N + 2) // 3
    if (power_of_2 & (power_of_2 - 1)) != 0 and power_of_2 != 1:
        print(-1)
        return
    
    D = power_of_2.bit_length() - 1

    graph = [[] for _ in range(N + 1)]
    degrees = [0] * (N + 1)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    if not all(degrees[i] in [1, 3] for i in range(1, N + 1)):
        print(-1)
        return

    u, _ = bfs(1, N, graph)
    v, dist_from_u = bfs(u, N, graph)
    
    if dist_from_u[v] != 2 * D:
        print(-1)
        return

    _, dist_from_v = bfs(v, N, graph)
    root_candidate = -1
    for i in range(1, N + 1):
        if dist_from_u[i] == D and dist_from_v[i] == D:
            root_candidate = i
            break
    
    if root_candidate != -1 and degrees[root_candidate] == 3:
        print(1)
        print(root_candidate)
    else:
        print(-1)

solve()