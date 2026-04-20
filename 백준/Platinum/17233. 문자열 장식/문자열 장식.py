import sys
import heapq
input = sys.stdin.readline

# 1. 입력 처리
N_str = input().split()
if not N_str:
    sys.exit()
N = int(N_str[0])

patterns = []
for _ in range(N):
    length_str, p_str = input().split()
    patterns.append(p_str)

S_length_str, S_str = input().split()
S_length = int(S_length_str)

# 2. 패턴 필터링 (불필요한 부분 문자열 제거)
patterns.sort(key=len, reverse=True)
filtered_P = []
for p in patterns:
    is_sub = False
    for fp in filtered_P:
        if p in fp:
            is_sub = True
            break
    if not is_sub:
        filtered_P.append(p)

# 3. On-Demand N-포인터 (최소 힙 활용)
heap = []
max_end = -1

# 초기화: 각 패턴의 첫 번째 등장 위치만 찾아서 힙에 삽입
for i in range(len(filtered_P)):
    p = filtered_P[i]
    start_idx = S_str.find(p)
    
    end_idx = start_idx + len(p)
    # 최소 힙은 시작 위치(start_idx)를 기준으로 정렬됨
    heapq.heappush(heap, (start_idx, i))
    
    if end_idx > max_end:
        max_end = end_idx

ans = float('inf')

# 4. 힙을 돌면서 최단 구간 갱신
while heap:
    # 가장 앞에 있는 패턴을 뽑음
    min_start, p_idx = heapq.heappop(heap)
    
    # 현재 윈도우의 길이로 정답 갱신 (max_end는 별도의 덱 없이 계속 누적 갱신됨)
    current_len = max_end - min_start
    if current_len < ans:
        ans = current_len
        
    # 방금 뽑은 패턴의 '다음' 등장 위치를 On-Demand로 탐색
    next_start = S_str.find(filtered_P[p_idx], min_start + 1)
    
    # 만약 더 이상 해당 패턴이 등장하지 않는다면, 
    # 모든 패턴을 포함하는 윈도우는 더 이상 만들 수 없으므로 탐색 즉시 종료
    if next_start == -1:
        break
        
    # 새로 찾은 등장 위치의 끝점 계산
    next_end = next_start + len(filtered_P[p_idx])
    
    # max_end 갱신 (새로운 끝점이 기존의 최대 끝점보다 크다면 갱신)
    if next_end > max_end:
        max_end = next_end
        
    # 새로 찾은 위치를 다시 힙에 삽입
    heapq.heappush(heap, (next_start, p_idx))

print(ans)