n = int(input())
balls = list(input())

moves = list()
# to the left
for color in ['R', 'B']:
    flag = False
    cnt = 0
    for i in range(n):
        if balls[i] != color:
            flag = True
        if i > 0 and balls[i] == color and flag:
            cnt += 1
    moves.append(cnt)

# to the right
for color in ['R', 'B']:
    flag = False
    cnt = 0
    for i in range(n - 1, -1, -1):
        if balls[i] != color:
            flag = True
        if i < n - 1 and balls[i] == color and flag:
            cnt += 1
    moves.append(cnt)

print(min(moves))