import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().rstrip().split())
    board = [input().rstrip() for _ in range(N)]
    dy = [[[[0] * (K + 1) for _ in range(2)] for _ in range(N)] for _ in range(N)]

    # 시작점에서 오른쪽, 아래쪽으로 출발
    if N > 1 and board[0][1] == '.':
        dy[0][1][0][0] = 1  # 오른쪽
    if N > 1 and board[1][0] == '.':
        dy[1][0][1][0] = 1  # 아래쪽

    for i in range(N):
        for j in range(N):
            for direction in range(2):  # 0: 오른쪽, 1: 아래쪽
                for turn in range(K + 1):
                    val = dy[i][j][direction][turn]
                    if val == 0 or board[i][j] == 'H':
                        continue
                    # 같은 방향으로 이동
                    ni, nj = i + (direction == 1), j + (direction == 0)
                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == '.':
                        dy[ni][nj][direction][turn] += val
                    # 방향 전환
                    if turn < K:
                        ndirection = 1 - direction
                        ni2, nj2 = i + (ndirection == 1), j + (ndirection == 0)
                        if 0 <= ni2 < N and 0 <= nj2 < N and board[ni2][nj2] == '.':
                            dy[ni2][nj2][ndirection][turn + 1] += val

    ans = 0
    for direction in range(2):
        for turn in range(K + 1):
            ans += dy[N - 1][N - 1][direction][turn]
    print(ans)