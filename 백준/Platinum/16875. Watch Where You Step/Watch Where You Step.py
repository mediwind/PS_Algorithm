import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 1. SCC (Kosaraju)
visited = [False] * n
order = []

def dfs(v):
    visited[v] = True
    for nxt in range(n):
        if graph[v][nxt] and not visited[nxt]:
            dfs(nxt)
    order.append(v)

for i in range(n):
    if not visited[i]:
        dfs(i)

# reverse graph
rgraph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            rgraph[j].append(i)

comp = [-1] * n
scc_id = 0

def rdfs(v):
    stack = [v]
    comp[v] = scc_id
    while stack:
        cur = stack.pop()
        for nxt in rgraph[cur]:
            if comp[nxt] == -1:
                comp[nxt] = scc_id
                stack.append(nxt)

for v in reversed(order):
    if comp[v] == -1:
        rdfs(v)
        scc_id += 1

# 2. SCC 크기
size = [0] * scc_id
for i in range(n):
    size[comp[i]] += 1

# 3. SCC DAG
dag = [set() for _ in range(scc_id)]
for i in range(n):
    for j in range(n):
        if graph[i][j] and comp[i] != comp[j]:
            dag[comp[i]].add(comp[j])

# 4. DAG reachability (bitset)
reach = [0] * scc_id

# topo order = reversed order of SCC creation
for i in range(scc_id - 1, -1, -1):
    mask = 0
    for nxt in dag[i]:
        mask |= (1 << nxt)
        mask |= reach[nxt]
    reach[i] = mask

# 5. 정답 계산

# 기존 간선 수
existing = sum(sum(row) for row in graph)

total_possible = 0

# (1) 같은 SCC 내부
for s in size:
    total_possible += s * (s - 1)

# (2) SCC 간
for i in range(scc_id):
    for j in range(scc_id):
        if i != j:
            if (reach[i] >> j) & 1:
                total_possible += size[i] * size[j]

# 최종: 추가 가능한 간선
print(total_possible - existing)