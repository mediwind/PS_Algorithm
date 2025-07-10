import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

dp = list()
ans_s, ans_e = -1, -1

for i in range(N):
    new_dp = list()
    
    new_dp.append((A[i], i))

    for or_val, start_idx in dp:
        new_or_val = or_val | A[i]
        
        if new_dp[-1][0] != new_or_val:
            new_dp.append((new_or_val, start_idx))

    for or_val, start_idx in new_dp:
        if or_val == K:
            ans_s = start_idx + 1
            ans_e = i + 1
            break
    
    if ans_s != -1:
        break
        
    dp = new_dp

if ans_s != -1:
    print(ans_s, ans_e)
else:
    print(-1)