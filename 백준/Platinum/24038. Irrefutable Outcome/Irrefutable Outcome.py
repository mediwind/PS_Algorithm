import sys
# input = sys.stdin.readline

t_str = input()
T = int(t_str.strip())

out = []

for test_case in range(1, T + 1):
    B = input().strip()
    N = len(B)
    
    wall_L = [N] * N
    last_wall = N
    for i in range(N - 2, -1, -1):
        if B[i] == B[i + 1]:
            last_wall = i
        wall_L[i] = last_wall
        
    wall_R = [-1] * N
    last_wall = -1
    for i in range(1, N):
        if B[i] == B[i - 1]:
            last_wall = i
        wall_R[i] = last_wall
        
    l = 0
    r = N - 1
    turn = 'I'
    
    while l <= r:
        options = []
        if B[l] == turn:
            options.append('L')
        if B[r] == turn:
            options.append('R')
            
        if not options:
            winner = 'O' if turn == 'I' else 'I'
            score = 1 + (r - l + 1)
            out.append(f"Case #{test_case}: {winner} {score}")
            break
            
        elif len(options) == 1:
            if options[0] == 'L':
                l += 1
            else:
                r -= 1
                
        else:
            wL = wall_L[l]
            if wL >= r:
                winL = True
                DL = r - l + 1
            else:
                winL = (B[wL] == turn)
                DL = wL - l + 1
                
            wR = wall_R[r]
            if wR <= l:
                winR = True
                DR = r - l + 1
            else:
                winR = (B[wR] == turn)
                DR = r - wR + 1
                
            if winL and winR:
                if DL <= DR:
                    l += 1
                else:
                    r -= 1
            elif winL:
                l += 1
            elif winR:
                r -= 1
            else:
                if DL >= DR:
                    l += 1
                else:
                    r -= 1
                    
        turn = 'O' if turn == 'I' else 'I'
        
    else:
        winner = 'O' if turn == 'I' else 'I'
        score = 1
        out.append(f"Case #{test_case}: {winner} {score}")

print('\n'.join(out))