import sys
input = sys.stdin.readline

n, m = map(int, input().split())

spells = []
for _ in range(m):
    data = list(map(int, input().split()))
    mask = 0
    # 비트마스킹으로 마법 상태 저장
    for card in data[1:]:
        mask |= (1 << (card - 1))
    spells.append(mask)

target = (1 << n) - 1

# 전체 마법을 절반으로 나눕니다.
mid = m // 2

# 왼쪽 절반 탐색 (0 ~ mid-1)
left_memo = {}
for subset in range(1 << mid):
    state = 0
    used = []
    
    for i in range(mid):
        if subset & (1 << i):
            state ^= spells[i]
            used.append(i + 1)
            
    count = len(used)
    used_tuple = tuple(used)
    
    # 딕셔너리에 최소 개수, 사전순 최적의 조합만 저장합니다.
    if state not in left_memo:
        left_memo[state] = (count, used_tuple)
    else:
        prev_count, prev_tuple = left_memo[state]
        if count < prev_count:
            left_memo[state] = (count, used_tuple)
        elif count == prev_count and used_tuple < prev_tuple:
            left_memo[state] = (count, used_tuple)

best_count = float('inf')
best_sequence = ()

# 오른쪽 절반 탐색 (mid ~ m-1)
right_size = m - mid
for subset in range(1 << right_size):
    state = 0
    used = []
    
    for i in range(right_size):
        if subset & (1 << i):
            state ^= spells[mid + i]
            used.append(mid + i + 1)
            
    # 전체를 target으로 만들기 위해 왼쪽에서 필요한 상태
    req_state = target ^ state
    
    if req_state in left_memo:
        left_count, left_tuple = left_memo[req_state]
        total_count = left_count + len(used)
        
        # 왼쪽 절반의 인덱스가 항상 작으므로 단순 연결만 해도 오름차순이 유지됩니다.
        total_sequence = left_tuple + tuple(used)
        
        # 최적의 결과 갱신
        if total_count < best_count:
            best_count = total_count
            best_sequence = total_sequence
        elif total_count == best_count and total_sequence < best_sequence:
            best_sequence = total_sequence

print(best_count)
print(*best_sequence)