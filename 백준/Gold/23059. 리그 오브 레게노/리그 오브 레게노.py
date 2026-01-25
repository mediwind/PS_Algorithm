import sys
input = sys.stdin.readline

N = int(input())

adj = {}
indegree = {}
all_items = set()

for _ in range(N):
    u, v = input().split()
    all_items.add(u)
    all_items.add(v)

    if u not in adj: adj[u] = []
    adj[u].append(v)

    if u not in indegree: indegree[u] = 0
    if v not in indegree: indegree[v] = 0

    indegree[v] += 1

current_batch = []
for item in all_items:
    if indegree[item] == 0:
        current_batch.append(item)

result = []

while current_batch:
    current_batch.sort()

    next_batch = []

    for u in current_batch:
        result.append(u)

        if u in adj:
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    next_batch.append(v)

    current_batch = next_batch

if len(result) != len(all_items):
    print(-1)
else:
    for item in result:
        print(item)