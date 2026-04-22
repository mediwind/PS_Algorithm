import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
c = int(input())

# 1. 포물선 공식을 1차 함수(직선)로 변환하여 저장
lines = []
for _ in range(N):
    x, y = map(int, input().split())
    # A_i = -2x_i, B_i = cy_i - x_i^2
    A = -2 * x
    B = c * y - x * x
    lines.append((A, B))

# 볼록 껍질 구성을 위해 기울기(A) 기준으로 오름차순 정렬
lines.sort()

# 기울기가 같은 직선 중에서는 절편(B)이 가장 큰 것만 남김
filtered_lines = []
for A, B in lines:
    if filtered_lines and filtered_lines[-1][0] == A:
        filtered_lines[-1] = (A, max(filtered_lines[-1][1], B))
    else:
        filtered_lines.append((A, B))

# 2. 볼록 껍질(Upper Envelope) 구성
stack = []
for A_new, B_new in filtered_lines:
    while len(stack) >= 2:
        A_curr, B_curr = stack[-1]
        A_prev, B_prev = stack[-2]
        
        # 교차점 X좌표 비교: x_{prev, curr} >= x_{curr, new} 이면 curr 직선은 무의미하므로 제거
        # (B_prev - B_curr) / (A_curr - A_prev) >= (B_curr - B_new) / (A_new - A_curr)
        # 기울기가 오름차순이므로 분모는 항상 양수. 나눗셈의 실수 오차를 피하기 위해 크로스 곱셈 수행
        left = (B_curr - B_new) * (A_curr - A_prev)
        right = (B_prev - B_curr) * (A_new - A_curr)
        
        if left <= right:
            stack.pop()
        else:
            break
    stack.append((A_new, B_new))

# 3. 쿼리 처리
queries = list(map(int, input().split()))
ans = []

for p in queries:
    # 이분 탐색을 통해 최적의 직선 찾기 (볼록성 이용)
    low = 0
    high = len(stack) - 1
    
    while low < high:
        mid = (low + high) // 2
        A_mid, B_mid = stack[mid]
        A_next, B_next = stack[mid+1]
        
        val_mid = A_mid * p + B_mid
        val_next = A_next * p + B_next
        
        # 다음 직선의 결과가 더 좋거나 같다면, 최댓값은 오른쪽에 있음
        if val_next >= val_mid:
            low = mid + 1
        else:
            high = mid
            
    best_A, best_B = stack[low]
    
    # 4. 공통적으로 생략했던 -p^2 을 더해서 최종 높이 분자값 계산
    best_val = best_A * p + best_B - p * p
    
    # 결과가 0 이하면 0 출력, 아니면 c로 나누어 실제 높이 출력
    if best_val <= 0:
        ans.append(0)
    else:
        ans.append(best_val / c)

# 한 번에 출력
print("\n".join(map(str, ans)))