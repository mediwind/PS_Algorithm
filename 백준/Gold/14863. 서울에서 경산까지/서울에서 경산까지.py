import sys
input = sys.stdin.readline

N, K = map(int, input().split())
prev = [-1 for _ in range(K + 1)]
prev[0] = 0

for _ in range(N):
    w_time, w_money, b_time, b_money = map(int, input().split())
    curr = [-1 for _ in range(K + 1)]
    
    for t in range(K + 1):
        if prev[t] == -1:
            continue
        
        if t + w_time <= K:
            curr[t + w_time] = max(curr[t + w_time], prev[t] + w_money)
        
        if t + b_time <= K:
            curr[t + b_time] = max(curr[t + b_time], prev[t] + b_money)
    
    prev = curr

print(max(prev))