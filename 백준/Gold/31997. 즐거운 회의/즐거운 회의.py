import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())

# 0.5 단위 t=0.5→t=0, 1.5→1, …, T-0.5→T-1 을
# int t=0…T-1 로 매핑
in_events  = [[] for _ in range(T+1)]
out_events = [[] for _ in range(T+1)]

# 참석/퇴장 시간
for i in range(N):
    a, b = map(int, input().split())
    in_events[a].append(i)
    out_events[b].append(i)

# 친구 인접 리스트
friends = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    friends[u].append(v)
    friends[v].append(u)

joined = [False]*N
total = 0
ans = []

for t in range(T):
    # (1) t+0.5 이전에 떠나는 사람들
    for u in out_events[t]:
        # 떠나기 전, u–v 쌍만큼 total-- 
        for v in friends[u]:
            if joined[v]:
                total -= 1
        joined[u] = False

    # (2) t+0.5 직전에 들어오는 사람들
    for u in in_events[t]:
        # 들어오기 전, u–v 쌍만큼 total++
        for v in friends[u]:
            if joined[v]:
                total += 1
        joined[u] = True

    # (3) t+0.5 순간의 총 친구 쌍
    ans.append(str(total))

print('\n'.join(ans))