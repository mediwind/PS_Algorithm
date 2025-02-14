import heapq as hq
import sys
input = sys.stdin.readline


def widest_path(x):
    # -inf도 가능하지만 0이 코드의 간결함과 가독성 측면에서 더 권장
    bandwidth = [0 for _ in range(n + 1)]
    # 0이 아닌 inf로 두어야 시작 노드 x의 첫 간선 대역폭이 그대로 반영됨
    bandwidth[x] = float("inf")
    
    # 최대 힙이므로 -를 붙여 음수 값으로 저장
    Q = list()
    hq.heappush(Q, (-float("inf"), x))
    
    while Q:
        current_bandwidth, node = hq.heappop(Q)
        current_bandwidth = -current_bandwidth
        
        # 이미 발견한 최대 대역폭 > 현재까지의 최소 대역폭인 경우 스킵
        if bandwidth[node] > current_bandwidth:
            continue
        
        if node == t:
            return bandwidth[t]
        
        for neighbor, weight in graph[node]:
            tmp = min(current_bandwidth, weight)
            
            if tmp > bandwidth[neighbor]:
                bandwidth[neighbor] = tmp
                hq.heappush(Q, (-tmp, neighbor))
    
    return 0


t = int(input())
for _ in range(t):
    n, m, s, t = map(int, input().strip().split())
    
    graph = [list() for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().strip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    print(widest_path(s))