import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 왼쪽에서 오른쪽으로
L_max = [0] * N # 구간합의 최대
L_min = [0] * N # 구간합의 최소

cur_max = arr[0]
cur_min = arr[0]
L_max[0] = arr[0]
L_min[0] = arr[0]

for i in range(1, N):
    cur_max = max(arr[i], cur_max + arr[i])
    cur_min = min(arr[i], cur_min + arr[i])
    
    L_max[i] = max(L_max[i - 1], cur_max)
    L_min[i] = min(L_min[i - 1], cur_min)

# 오른쪽에서 왼쪽으로
R_max = [0] * N
R_min = [0] * N

cur_max = arr[N - 1]
cur_min = arr[N - 1]
R_max[N - 1] = arr[N - 1]
R_min[N - 1] = arr[N - 1]

for i in range(N - 2, -1, -1):
    cur_max = max(arr[i], cur_max + arr[i])
    cur_min = min(arr[i], cur_min + arr[i])
    
    R_max[i] = max(R_max[i + 1], cur_max)
    R_min[i] = min(R_min[i + 1], cur_min)

# 자르기와 정답 찾기
ans = float('-inf')
for k in range(1, N): # 최소 한 명씩은 팀을 구성하므로 1부터 N - 1까지
    case1 = L_max[k - 1] * R_max[k] # 양수 최대
    case2 = L_min[k - 1] * R_min[k] # 음수 최소 (곱할 경우 양수 최대)
    # 혹시 모를 양수 * 음수 등 모든 조합 중 최대
    case3 = L_max[k - 1] * R_min[k]
    case4 = L_min[k - 1] * R_max[k]
    
    ans = max(ans, case1, case2, case3, case4)

print(ans)