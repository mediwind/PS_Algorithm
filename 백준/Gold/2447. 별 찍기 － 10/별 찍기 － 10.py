def DFS(n):
#     global board # 전역 변수 여부 상관 X
    if n == 3:
        board[0][:3] = board[2][:3] = ['*'] * 3
        board[1][:3] = ['*', ' ', '*']
        return
    
    a = n // 3
    DFS(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                board[a * i + k][a * j:a * (j + 1)] = board[k][:a]


n = int(input())

board = [[' ' for _ in range(n)] for _ in range(n)]
DFS(n)
for b in board:
    print(''.join(b))