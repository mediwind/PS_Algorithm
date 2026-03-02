import sys
from collections import deque
input = sys.stdin.readline


def evaluate_direction(p_arr, d_arr):
    A = [0] * (2 * N)
    for i in range(N):
        A[i] = p_arr[i] - d_arr[i]
        A[i + N] = p_arr[i] - d_arr[i]
        
    S = [0] * (2 * N + 1)
    for i in range(2 * N):
        S[i + 1] = S[i] + A[i]
        
    valid = [False] * N
    dq = deque()
    
    for i in range(2 * N + 1):
        while dq and dq[0] < i - N:
            dq.popleft()
            
        while dq and S[dq[-1]] >= S[i]:
            dq.pop()
            
        dq.append(i)
        
        if i >= N:
            start_idx = i - N
            if start_idx < N:
                if S[dq[0]] - S[start_idx] >= 0:
                    valid[start_idx] = True
                    
    return valid


N = int(input().strip())

P = [0] * N
D = [0] * N

for i in range(N):
    p, d = map(int, input().split())
    P[i] = p
    D[i] = d

cw_valid = evaluate_direction(P, D)

P_ccw = [0] * N
D_ccw = [0] * N

for i in range(N):
    P_ccw[i] = P[(N - i) % N]
    D_ccw[i] = D[(N - i - 1) % N]

ccw_valid_mapped = evaluate_direction(P_ccw, D_ccw)

ccw_valid = [False] * N
for i in range(N):
    if ccw_valid_mapped[i]:
        ccw_valid[(N - i) % N] = True

for i in range(N):
    if cw_valid[i] or ccw_valid[i]:
        print("TAK")
    else:
        print("NIE")