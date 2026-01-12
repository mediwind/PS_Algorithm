import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

# 정답을 저장할 변수 (최댓값을 찾아야 하므로 아주 작은 수로 초기화)
ans = -float('inf')

# 1. Case 1: 좌상단 -> 우하단 (↘️ 방향) 이동
# 이동 가능 방향: 위(Up)에서 오거나, 왼쪽(Left)에서 오는 경우를 받음
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 이전 경로 중 최댓값 (범위 벗어나면 0 처리)
        # max(0, ...)을 통해 이전 경로 합이 음수면 버림 (새로 시작)
        prev_max = 0
        
        # 위쪽에서 오는 경우
        if i > 0:
            prev_max = max(prev_max, dp[i-1][j])
        # 왼쪽에서 오는 경우
        if j > 0:
            prev_max = max(prev_max, dp[i][j-1])
            
        dp[i][j] = grid[i][j] + prev_max
        
        # 전체 최댓값 갱신
        if dp[i][j] > ans:
            ans = dp[i][j]

# 2. Case 2: 좌하단 -> 우상단 (↗️ 방향) 이동
# 이동 가능 방향: 아래(Down)에서 오거나, 왼쪽(Left)에서 오는 경우를 받음
# dp 배열 초기화
dp = [[0] * M for _ in range(N)]

# 행을 역순으로 순회 (N-1 -> 0)
for i in range(N - 1, -1, -1):
    for j in range(M):
        prev_max = 0
        
        # 아래쪽에서 오는 경우 (현재 i보다 큰 행에서 옴)
        if i < N - 1:
            prev_max = max(prev_max, dp[i+1][j])
        # 왼쪽에서 오는 경우
        if j > 0:
            prev_max = max(prev_max, dp[i][j-1])
            
        dp[i][j] = grid[i][j] + prev_max
        
        if dp[i][j] > ans:
            ans = dp[i][j]

print(ans)