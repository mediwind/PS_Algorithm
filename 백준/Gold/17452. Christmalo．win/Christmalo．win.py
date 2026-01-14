import sys
input = sys.stdin.readline

INF = float('inf')

N = int(input().strip())

best_fronts = [[(INF, -1), (INF, -1)] for _ in range(26)]
best_backs = [[(INF, -1), (INF, -1)] for _ in range(26)]

for i in range(N):
    S = input().strip()
    L = len(S)
    
    first_occ = [-1] * 26
    last_occ = [-1] * 26
    
    for idx, char in enumerate(S):
        code = ord(char) - 97 # 'a' -> 0, 'z' -> 25
        if first_occ[code] == -1:
            first_occ[code] = idx
        last_occ[code] = idx
        
    for code in range(26):
        if first_occ[code] != -1:
            b_cost = first_occ[code]
            curr_backs = best_backs[code]
            
            if b_cost < curr_backs[0][0]:
                curr_backs[1] = curr_backs[0]
                curr_backs[0] = (b_cost, i)
            elif b_cost < curr_backs[1][0]:
                curr_backs[1] = (b_cost, i)

            f_cost = L - 1 - last_occ[code]
            curr_fronts = best_fronts[code]
            
            if f_cost < curr_fronts[0][0]:
                curr_fronts[1] = curr_fronts[0]
                curr_fronts[0] = (f_cost, i)
            elif f_cost < curr_fronts[1][0]:
                curr_fronts[1] = (f_cost, i)

min_ans = INF

for code in range(26):
    ff = best_fronts[code]
    bb = best_backs[code]
    
    if ff[0][0] == INF or bb[0][0] == INF:
        continue
        
    for f_cand in ff:
        for b_cand in bb:
            if f_cand[0] != INF and b_cand[0] != INF:
                if f_cand[1] != b_cand[1]:
                    min_ans = min(min_ans, f_cand[0] + b_cand[0])

if min_ans == INF:
    print(-1)
else:
    print(min_ans)