import sys
input = sys.stdin.readline
sys.setrecursionlimit(200005)

n_str = input().strip()
if not n_str:
    sys.exit()
N = int(n_str)

# 1. 트리 구성 (단방향)
adj = [[] for _ in range(N + 1)]
if N > 1:
    parents = list(map(int, input().split()))
    for i in range(2, N + 1):
        adj[parents[i - 2]].append(i)

# dp[u][0]: u가 팔/다리이거나 자유로울 때 (내부 완성본)
# dp[u][1]: u가 골반일 때
# dp[u][2]: u가 가슴일 때
dp = [[0, 0, 0] for _ in range(N + 1)]
# best[u] = max(dp[u][0], dp[u][2] + 1) (u가 낼 수 있는 진정한 최대 가치)
best = [0] * (N + 1)

def dfs(u):
    sum_best = 0
    losses_0 = []
    
    # 1단계: 자식들의 진정한 최대 가치를 모두 더하고, 팔/다리로 강제할 때의 기회비용 계산
    for v in adj[u]:
        dfs(v)
        sum_best += best[v]
        
        # v를 팔/다리(State 0)로 썼을 때 잃어버리는 손실
        loss0 = best[v] - dp[v][0]
        losses_0.append((loss0, v))
        
    # [State 0] 자유 상태: 자식들이 자유롭게 최선을 다한 결과 합산
    dp[u][0] = sum_best
    
    # [State 1] 골반 상태: 손실이 가장 적은 2개의 자식을 다리로 차출
    if len(adj[u]) >= 2:
        losses_0.sort()
        dp[u][1] = sum_best - losses_0[0][0] - losses_0[1][0]
    else:
        dp[u][1] = -float('inf')
        
    # [State 2] 가슴 상태: 1개의 골반과 2개의 팔 차출
    if len(adj[u]) >= 3:
        # 팔로 쓸 자식을 고를 때 탐색 시간을 줄이기 위해, 손실이 적은 상위 3개만 잘라냄 O(1)
        top3_losses = losses_0[:3]
        best_chest = -float('inf')
        
        # 어떤 자식 v를 골반(Pelvis)으로 쓸지 모두 순회해봄
        for v in adj[u]:
            loss_p = best[v] - dp[v][1]
            
            arm_losses = 0
            arms_picked = 0
            # v를 제외한 나머지 자식 중 가장 손실이 적은 2개를 팔(Arm)로 선택
            for loss0, child_v in top3_losses:
                if child_v == v:
                    continue
                arm_losses += loss0
                arms_picked += 1
                if arms_picked == 2:
                    break
                    
            best_chest = max(best_chest, sum_best - loss_p - arm_losses)
        dp[u][2] = best_chest
    else:
        dp[u][2] = -float('inf')
        
    # 현재 노드 u가 낼 수 있는 진정한 최대 가치 갱신
    best[u] = max(dp[u][0], dp[u][2] + 1)

dfs(1)

# 루트 노드(1)는 부모가 없으므로 가슴이나 골반이 될 수 없고, 온전히 내부의 값(dp[1][0])이 정답이 됨
print(dp[1][0])