from collections import deque
import sys
input = sys.stdin.readline

test_count = int(input())

for _ in range(test_count):
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    queue = deque()
    order = []

    last_year_rank = list(map(int, input().split()))

    for i in range(n - 1):
        for j in range(i + 1, n):
            higher = last_year_rank[i]
            lower = last_year_rank[j]

            graph[higher].append(lower)
            indegree[lower] += 1

    change_count = int(input())

    for _ in range(change_count):
        team_a, team_b = map(int, input().split())

        reversed_edge = True

        for nxt in graph[team_a]:
            if nxt == team_b:
                graph[team_a].remove(team_b)
                indegree[team_b] -= 1

                graph[team_b].append(team_a)
                indegree[team_a] += 1

                reversed_edge = False
                break

        if reversed_edge:
            graph[team_b].remove(team_a)
            indegree[team_a] -= 1

            graph[team_a].append(team_b)
            indegree[team_b] += 1

    for node in range(1, n + 1):
        if indegree[node] == 0:
            queue.append(node)

    if not queue:
        print("IMPOSSIBLE")
        continue

    is_valid = True

    while queue:
        if len(queue) > 1:
            is_valid = False
            break

        cur = queue.popleft()
        order.append(cur)

        for nxt in graph[cur]:
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                queue.append(nxt)
            elif indegree[nxt] < 0:
                is_valid = False
                break

    if not is_valid or len(order) < n:
        print("IMPOSSIBLE")
    else:
        print(*order)