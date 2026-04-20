import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
patterns = []
for _ in range(N):
    length_str, p_str = input().split()
    patterns.append(p_str)

S_length_str, S = input().split()
S_length = int(S_length_str)

# 1. 패턴 필터링 (기존과 동일하게 불필요한 부분 문자열 제거)
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

# 2. 파이썬 내장 C엔진(find)을 이용한 초고속 위치 탐색
events = []
for i, p in enumerate(filtered_P):
    p_len = len(p)
    idx = S.find(p)
    # KMP와 동일하게 겹치는 구간을 모두 찾기 위해 시작점을 1씩 밀면서 탐색
    while idx != -1:
        # (시작 인덱스, 끝 인덱스, 패턴 번호) 튜플로 저장
        events.append((idx, idx + p_len, i))
        idx = S.find(p, idx + 1)

# 3. 투 포인터(Sliding Window)와 단조 큐(Monotonic Queue)를 활용한 N-포인터 최적화
events.sort(key=lambda x: x[0])  # 시작 인덱스 기준으로 오름차순 정렬

M = len(filtered_P)
ans = float('inf')

counts = [0] * M       # 현재 윈도우 안의 각 패턴 개수
unique_count = 0       # 윈도우 안에 존재하는 서로 다른 패턴의 종류 수
left = 0
q = deque()            # 현재 윈도우 내 '끝나는 인덱스'의 최댓값을 추적하기 위한 덱

# right 포인터를 하나씩 늘려가며 윈도우를 확장
for right in range(len(events)):
    start, end, pid = events[right]
    
    # 새로운 패턴이 추가됨
    if counts[pid] == 0:
        unique_count += 1
    counts[pid] += 1
    
    # 단조 큐 유지: 새로 들어온 구간의 끝점보다 작거나 같은 기존 끝점들은 덱에서 제거 (가장 멀리 뻗은 끝점만 알면 되기 때문)
    while q and events[q[-1]][1] <= end:
        q.pop()
    q.append(right)
    
    # 모든 종류의 패턴이 윈도우 안에 모였다면 (조건 만족)
    while unique_count == M:
        # q[0]는 항상 현재 윈도우 안에서 가장 큰 끝(end) 값을 가짐
        max_end = events[q[0]][1]
        min_start = events[left][0]
        
        # 정답 갱신
        if max_end - min_start < ans:
            ans = max_end - min_start
            
        # left 포인터를 당기기 위해 기존 left가 가리키던 패턴 제거
        remove_pid = events[left][2]
        counts[remove_pid] -= 1
        if counts[remove_pid] == 0:
            unique_count -= 1
            
        # 만약 덱의 최댓값이 방금 윈도우에서 빠진 left 인덱스였다면 덱에서도 제거
        if q[0] == left:
            q.popleft()
            
        left += 1

print(ans)