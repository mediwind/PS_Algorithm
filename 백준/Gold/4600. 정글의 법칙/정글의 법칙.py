import sys
input = sys.stdin.readline

while True:
    B, P = map(int, input().rstrip().split())
    B = -B
    
    if B == 0 and P == 0:
        break
        
    bridges = list()
    for _ in range(B):
        C, T = map(int, input().rstrip().split())
        bridges.append((C, T))

    n = len(bridges)
    waiting = [0 for _ in range(n)]
    on_bridge = [0 for _ in range(n)]
    time_off = [-1 for _ in range(n)]

    waiting[0] = P
    done = 0
    cur_time = 0

    while done < P:
        # 다음 이벤트 시간 계산
        next_time = cur_time
        found = False
        for i in range(n):
            if waiting[i] > 0 and on_bridge[i] == 0:
                found = True
                break
        if not found:
            next_time = float('inf')
            for t in time_off:
                if t != -1:
                    next_time = min(next_time, t)
        cur_time = next_time

        # 다리 건너기 완료 처리
        for i in range(n):
            if on_bridge[i] > 0 and time_off[i] == cur_time:
                group = on_bridge[i]
                on_bridge[i] = 0
                time_off[i] = -1
                if i < n - 1:
                    waiting[i + 1] += group
                else:
                    done += group

        # 다리 건너기 시작 처리
        for i in range(n):
            if waiting[i] > 0 and on_bridge[i] == 0:
                cap, dur = bridges[i]
                group = min(cap, waiting[i])
                on_bridge[i] = group
                waiting[i] -= group
                time_off[i] = cur_time + dur

    print(cur_time)