import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
birds_pref = []
delta = [0]*M

for _ in range(N):
    side, s = input().rstrip().split()
    sign = 1 if side == 'R' else -1
    pref = [0]*M
    run = 0
    for i, ch in enumerate(s):
        if ch == '1':
            run += sign
            delta[i] += sign
        pref[i] = run
    birds_pref.append(pref)

S = [0]*M
run = 0
for i in range(M):
    run += delta[i]
    S[i] = run

best_idx = 0
best_val = 10**9
for idx, pref in enumerate(birds_pref):
    mv = 0
    for i in range(M):
        v = S[i] - pref[i]
        if v < 0:
            v = -v
        if v > mv:
            mv = v
            if mv >= best_val:
                break
    else:
        pass
    if mv < best_val:
        best_val = mv
        best_idx = idx

print(best_idx+1)
print(best_val)