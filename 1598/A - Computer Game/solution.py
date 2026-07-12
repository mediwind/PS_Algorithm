import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(2)]
    
    for i in range(n):
        if board[0][i] and board[1][i]:
            print("NO")
            break
    else:
        print("YES")