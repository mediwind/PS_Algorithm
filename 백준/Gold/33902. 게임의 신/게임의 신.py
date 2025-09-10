import math


def DFS(x, y):
    if (x, y) in dp:
        return dp[(x, y)]

    moves = list()
    for z in range(x+1, y+1):
        if math.gcd(x, z) == 1:
            moves.append(z)

    if not moves:
        dp[(x, y)] = False
        return False

    for next_x in moves:
        if not DFS(next_x, y):
            dp[(x, y)] = True
            return True

    dp[(x, y)] = False
    return False


X, Y = map(int, input().split())

dp = dict()

if DFS(X, Y):
    print("khj20006")
else:
    print("putdata")