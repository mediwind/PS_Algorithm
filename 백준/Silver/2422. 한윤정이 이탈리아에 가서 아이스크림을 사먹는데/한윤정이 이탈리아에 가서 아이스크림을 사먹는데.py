from itertools import combinations
# import sys
# input = sys.stdin.readline

n, m = map(int, input().split())
board = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = True
    board[b - 1][a - 1] = True

cnt = 0
for comb in combinations(list(range(n)), 3):
    one, two, three = comb
    if board[one][two] or board[two][three] or board[one][three]:
        continue
    cnt += 1

print(cnt)