import sys
input = sys.stdin.readline

# 1. 입력 처리
N_str = input().split()
if not N_str:
    sys.exit(0)
N = int(N_str[0])
M = int(N_str[1])

A = input().strip()

# 2. 누적합 배열 P 생성
P = [0] * (N + 1)
for i in range(1, N + 1):
    if A[i - 1] == '(':
        P[i] = P[i - 1] + 1
    else:
        P[i] = P[i - 1] - 1

# 3. 상태 추적 배열 미리 계산 (Right-to-Left Sweep)
drop = [float('inf')] * (N + 1)
equal_nxt = [float('inf')] * (N + 1)

# 누적합 값은 음수도 가능하므로, 인덱스 매핑을 위해 N+1만큼의 오프셋을 줍니다.
offset = N + 1
last_seen = [float('inf')] * (2 * N + 2)

for i in range(N, -1, -1):
    val = P[i] + offset
    
    # 처음으로 기준선 아래로 떨어지는 지점
    drop[i] = last_seen[val - 1]
    
    # 처음으로 기준선과 다시 같아지는 지점 (VBS의 첫 번째 쪼개짐 포인트)
    equal_nxt[i] = last_seen[val]
    
    # 현재 값을 가장 최근에 본 인덱스로 갱신
    last_seen[val] = i

# 4. 쿼리 처리 O(1)
ans = []
for _ in range(M):
    L, R = map(int, input().split())
    L_minus_1 = L - 1
    
    # 조건 1: 전체 괄호의 짝이 맞지 않는 경우
    if P[R] != P[L_minus_1]:
        ans.append("EI")
    # 조건 2: 구간 내에서 한 번이라도 기준점 아래로 떨어지는 경우 (올바른 괄호가 아님)
    elif drop[L_minus_1] <= R:
        ans.append("EI")
    # 조건 3: 구간 내에서 기준점으로 돌아오는 지점이 R 이전에 없는 경우 (쪼갤 수 없음)
    elif equal_nxt[L_minus_1] >= R:
        ans.append("EI")
    # 모든 조건을 통과하면 성공
    else:
        ans.append("JAH")

# 빠른 출력을 위해 배열에 모아서 한 번에 출력
print("\n".join(ans))