import sys
input = sys.stdin.readline


def growing(growth):
    arr = [0] * growth[0]
    arr.extend([1] * growth[1])
    arr.extend([2] * growth[2])
#     print(arr)
    
    idx = 0
    for i in range(m - 1, -1, -1):
        board[i][0] += arr[idx]
        idx += 1
    
    for i in range(1, m):
        board[0][i] += arr[idx]
        idx += 1


m, n = map(int, input().split())
board = [[1 for _ in range(m)] for _ in range(m)]

for _ in range(n):
    growth = list(map(int, input().split()))
    growing(growth)

for i in range(1, m):
    for j in range(1, m):
        board[i][j] = max(board[i][j - 1], board[i - 1][j - 1], board[i - 1][j])

for bd in board:
    print(*bd)