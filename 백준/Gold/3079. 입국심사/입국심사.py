import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
times.sort()

lt = times[0] # 가장 빠른 심사대에서 1명 심사하는 시간
rt = times[-1] * m # 가장 느린 심사대에서 m명 모두 심사하는 시간
ans = float('inf')

while lt <= rt:
    mid = (lt + rt)//2
    total = 0
    for time in times:
        total += mid//time # mid 시간이 주어졌을 때 각 심사대별 최대한 심사할 수 있는 인원 누적
        
    if total >= m: # 심사대들을 동원하여 m명을 mid 시간내에 처리 가능하다면
        rt = mid - 1 # 심사 시간 최소화를 위해 rt의 범위 축소
        ans = min(ans, mid)
    else: # 그렇지 못하다면
        lt = mid + 1 # 심사 시간 탐색 및 화갣를 위해 rt의 범위 확대

print(ans)