import sys
input = sys.stdin.readline

n, k = map(int, input().split())
u = list(map(int, input().split()))

# V: 초기 상태에서 무대를 볼 수 있는 관람객 정보 저장 (인덱스, 키)
V = []
max_h = -1

# 1. 시야가 확보된 기본 관람객 찾기
for i in range(n):
    if u[i] > max_h:
        V.append((i, u[i]))
        max_h = u[i]
        
m = len(V)
available_costs = []

i = 0
# 2. 관람객들을 연속된 키(H, H+1, H+2...)를 가진 '블록'으로 그룹화
while i < m:
    start = i
    end = i
    
    # 다음 관람객의 키가 정확히 1 크다면 같은 블록으로 묶음
    while end + 1 < m and V[end + 1][1] == V[end][1] + 1:
        end += 1
        
    S = end - start + 1 # 현재 블록 크기
    min_cost = -1
    
    # 3. 해당 블록 내에서 1명을 추가하기 위한 최소 비용(Cost) 계산
    for j in range(end, start - 1, -1):
        seg_start = V[j][0] + 1
        seg_end = V[j + 1][0] if j + 1 < m else n
        
        has_candidate = False
        # V[j]와 다음 관람객 사이에 V[j][1]과 키가 정확히 같은 '후보'가 있는지 확인
        for idx in range(seg_start, seg_end):
            if u[idx] == V[j][1]:
                has_candidate = True
                break
                
        if has_candidate:
            # 후보를 위한 의자 1개 + 뒤이어 시야가 가려지는 기존 관람객 복구 비용
            min_cost = S - (j - start)
            break
            
    # 유효한 비용이 산출되었다면 목록에 추가
    if min_cost != -1:
        available_costs.append(min_cost)
        
    i = end + 1
    
# 4. 비용(Cost)을 오름차순으로 정렬하여 그리디 알고리즘 적용
available_costs.sort()

ans = m # 기본 관람객 수
for cost in available_costs:
    if k >= cost:
        k -= cost
        ans += 1
    else:
        break
        
print(ans)