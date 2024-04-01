from collections import defaultdict
from itertools import combinations


def DFS(L):
    global cnt
    if L == 15:
        cnt = 1
        for val in score_board.values():
            if sum(val):
                cnt = 0
                break
        return
    
    c1, c2 = games[L]
    for x, y in [(0, 2), (1, 1), (2, 0)]:
        if score_board[c1][x] and score_board[c2][y]:
            score_board[c1][x] -= 1
            score_board[c2][y] -= 1
            DFS(L + 1)
            score_board[c1][x] += 1
            score_board[c2][y] += 1


score_board = defaultdict(list)
country = [chr(i) for i in range(65, 71)]
games = list()
for comb in combinations(country, 2):
    games.append(comb)
# games

answer = list()
for _ in range(4):
    arr = list(map(int, input().split()))
    res = [arr[i:i+3] for i in range(0, 18, 3)]
    for i in range(6):
        score_board[chr(i + 65)] = res[i]
#     score_board

    cnt = 0
    DFS(0)
    answer.append(cnt)

print(*answer)