import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 인접 리스트
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 배신자 번호
betrayer = int(input())

visited = [False for _ in range(n + 1)]
max_group = 0
cycle_marker = -1

def dfs(node, parent, root, detect_cycle):
    """
    detect_cycle=True  : 시작점(root)==betrayer에서 사이클 탐색 모드
    detect_cycle=False : 단순 컴포넌트 크기 탐색 모드
    returns 이 서브트리(또는 서브그룹)의 노드 개수
    """
    global max_group, cycle_marker

    # 1) 배신자 주변 사이클 발견
    if detect_cycle:
        for w in graph[node]:
            if visited[w] and w == root and parent != root and cycle_marker == -1:
                cycle_marker = node
                break

    # 2) 본격 DFS: 자기 자신 포함 1
    size = 1
    for w in graph[node]:
        if not visited[w]:
            visited[w] = True
            # root==betrayer 일 때만 별도 처리를 한다
            if node == root and detect_cycle:
                # betrayer의 바로 다음 서브트리 크기를 구해보고 +1
                sub = dfs(w, node, root, detect_cycle) + 1
                max_group = max(max_group, sub)
                # 매 서브트리 끝나면 cycle_marker 초기화
                cycle_marker = -1
            else:
                # 일반 모드
                cnt = dfs(w, node, root, detect_cycle)
                size += cnt
                max_group = max(max_group, size)
    # 3) cycle_marker 위치에서 리턴값 조정
    if node == cycle_marker:
        return size - 1
    return size

# (A) betrayer가 속한 컴포넌트: detect_cycle=True
visited[betrayer] = True
dfs(betrayer, 0, betrayer, True)

# (B) 나머지 컴포넌트: detect_cycle=False
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i, 0, i, False)

# Special case: n==1
if n == 1:
    print(1)
else:
    print(max_group)