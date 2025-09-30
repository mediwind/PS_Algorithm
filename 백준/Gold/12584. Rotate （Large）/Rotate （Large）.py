import sys
# input = sys.stdin.readline

def has(ch):
    for i in range(N):
        for j in range(N):
            
            if R[i][j] != ch:
                continue
                
            for di,dj in dirs:
                cnt = 1
                ni, nj = i + di, j + dj
                while 0 <= ni < N and 0 <= nj < N and R[ni][nj] == ch:
                    cnt += 1
                    
                    if cnt >= K:
                        return True
                    
                    ni += di
                    nj += dj
                    
    return False

dirs = [(0,1),(1,0),(1,1),(-1,1)]

T = int(input().rstrip())
for tc in range(1, T + 1):
    N, K = map(int, input().rstrip().split())
    A = [list(input().rstrip().strip()) for _ in range(N)]
    
    R = [['.'] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            R[j][N - 1 - i] = A[i][j]
    
    for c in range(N):
        col = [R[r][c] for r in range(N) if R[r][c] != '.']
        top = N - len(col)
        for r in range(top):
            R[r][c] = '.'
        for idx, ch in enumerate(col):
            R[top + idx][c] = ch
    
    red = has('R')
    blue = has('B')
    if red and blue: ans = "Both"
    elif red: ans = "Red"
    elif blue: ans = "Blue"
    else: ans = "Neither"
    print(f"Case #{tc}: {ans}")