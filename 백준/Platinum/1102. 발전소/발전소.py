import sys
input = sys.stdin.readline

n = int(input().strip())

# 비용 행렬 입력
cost = [list(map(int, input().split())) for _ in range(n)]

initial_state_str = input().strip()
p = int(input().strip())

initial_mask = 0
active_count = 0

# 주어진 Y/N 상태를 비트마스크 정수로 변환합니다.
for i in range(n):
    if initial_state_str[i] == 'Y':
        initial_mask |= (1 << i)
        active_count += 1

# 예외 처리 1: 이미 목표치 P개 이상 켜져 있는 경우
if active_count >= p:
    print(0)
    sys.exit(0)

# 예외 처리 2: 켜진 발전소가 하나도 없는데 켜야 할 발전소가 있는 경우
if active_count == 0 and p > 0:
    print(-1)
    sys.exit(0)

# DP 배열 초기화 (무한대)
INF = float('inf')
dp = [INF] * (1 << n)
dp[initial_mask] = 0

# 0부터 (2^N - 1)까지 모든 상태를 순회하는 Bottom-up 방식
for mask in range(1 << n):
    # 아직 도달할 수 없는 상태라면 건너뜁니다.
    if dp[mask] == INF:
        continue

    # 현재 상태에서 켜져 있는 발전소의 개수를 셉니다.
    current_active = bin(mask).count('1')

    # 이미 P개를 만족했다면, 비용은 음수가 아니므로 여기서 더 켜는 것은 최소 비용 탐색에 불필요합니다.
    if current_active >= p:
        continue

    # 켜진 발전소 i를 이용해 꺼진 발전소 j를 켭니다.
    for i in range(n):
        # i번 발전소가 켜져 있는지 확인
        if mask & (1 << i):
            for j in range(n):
                # j번 발전소가 꺼져 있는지 확인
                if not (mask & (1 << j)):
                    # j번 발전소를 켠 새로운 상태
                    next_mask = mask | (1 << j)
                    
                    # 최소 비용 갱신
                    if dp[mask] + cost[i][j] < dp[next_mask]:
                        dp[next_mask] = dp[mask] + cost[i][j]

# 정답 도출: 켜진 발전소가 P개 이상인 모든 상태 중 최소 비용을 찾습니다.
ans = INF
for mask in range(1 << n):
    if bin(mask).count('1') >= p:
        if dp[mask] < ans:
            ans = dp[mask]

print(ans)