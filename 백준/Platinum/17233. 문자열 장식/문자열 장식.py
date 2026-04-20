import sys
import heapq
input = sys.stdin.readline

N = int(input())
patterns = []
for _ in range(N):
    length_str, p_str = input().split()
    patterns.append(p_str)

S_length_str, S = input().split()
S_length = int(S_length_str)

# 1. 패턴 필터링 (불필요한 부분 문자열 제거)
# 길이가 긴 문자열부터 확인하기 위해 내림차순 정렬
patterns.sort(key=len, reverse=True)
filtered_P = []
for p in patterns:
    is_sub = False
    for fp in filtered_P:
        # 더 긴 문자열 안에 p가 이미 포함되어 있다면 제외
        if p in fp:
            is_sub = True
            break
    if not is_sub:
        filtered_P.append(p)

# 2. KMP 알고리즘을 이용한 패턴 위치 찾기
pos = []
for p in filtered_P:
    p_len = len(p)
    
    # LPS(Longest Prefix Suffix) 배열 생성
    lps = [0] * p_len
    j = 0
    for i in range(1, p_len):
        while j > 0 and p[i] != p[j]:
            j = lps[j - 1]
        if p[i] == p[j]:
            j += 1
            lps[i] = j
            
    # KMP 탐색을 통한 모든 등장 위치(시작 인덱스) 기록
    occurrences = []
    j = 0
    for i in range(S_length):
        while j > 0 and S[i] != p[j]:
            j = lps[j - 1]
        if S[i] == p[j]:
            if j == p_len - 1:
                occurrences.append(i - p_len + 1)
                j = lps[j]
            else:
                j += 1
    pos.append(occurrences)

# 3. N-포인터(최소 힙)를 이용한 최단 구간 찾기
heap = []
max_end = -1

# 초기화: 각 패턴의 첫 번째 등장 위치를 힙에 삽입하고, 가장 멀리 있는 끝점을 찾음
for i in range(len(filtered_P)):
    start_idx = pos[i][0]
    heapq.heappush(heap, (start_idx, i))
    
    end_idx = start_idx + len(filtered_P[i])
    if end_idx > max_end:
        max_end = end_idx

ptr = [0] * len(filtered_P)
ans = float('inf')

while True:
    # 현재 윈도우에서 가장 앞에 있는(가장 작은) 시작점을 뽑음
    min_start, p_idx = heapq.heappop(heap)
    
    # 현재 윈도우의 길이로 정답 갱신
    current_len = max_end - min_start
    if current_len < ans:
        ans = current_len
        
    # 가장 앞에 있던 포인터를 한 칸 뒤로 이동
    ptr[p_idx] += 1
    
    # 만약 어떤 패턴의 등장 위치를 끝까지 다 썼다면 더 이상 조건을 만족할 수 없으므로 종료
    if ptr[p_idx] == len(pos[p_idx]):
        break
        
    # 새로 이동한 위치를 힙에 넣고, 필요하다면 max_end 갱신
    next_start = pos[p_idx][ptr[p_idx]]
    next_end = next_start + len(filtered_P[p_idx])
    
    if next_end > max_end:
        max_end = next_end
        
    heapq.heappush(heap, (next_start, p_idx))

print(ans)