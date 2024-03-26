from itertools import combinations


def scoring(team):
    team1, team2 = list(), list()
    for i in range(1, n + 1):
        if i in team:
            team1.append(i)
        else:
            team2.append(i)

    score1 = 0
    for comb in combinations(team1, 2):
        x, y = comb
        x, y = x - 1, y - 1
        score1 += board[x][y]
        score1 += board[y][x]

    score2 = 0
    for comb in combinations(team2, 2):
        x, y = comb
        x, y = x - 1, y - 1
        score2 += board[x][y]
        score2 += board[y][x]

#     print('team:', team)
#     print(team1, team2)
#     print(score1, score2)
    
    return abs(score1 - score2)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

cand = list(range(1, n + 1))
min_score = float('inf')
for i in range(1, n//2 + 1):
    for comb in combinations(cand, i):
#         print(comb)
        res = scoring(comb)
        min_score = min(min_score, res)

print(min_score)