import sys
input = sys.stdin.readline

K = int(input())
for k in range(1, K + 1):
    M, N, P = map(int, input().split())
    failure_count = {i + 1: {j: 0 for j in range(M)} for i in range(P)}
#     failure_count

    score_board = {i + 1: {j: 0 for j in range(M)} for i in range(P)}
#     score_board

    for _ in range(N):
        p, m, t, j = input().split()
        p, t, j = map(int, [p, t, j])
        if j and not score_board[p][ord(m) - 65]:
            score_board[p][ord(m) - 65] = t + (failure_count[p][ord(m) - 65] * 20)
        elif not j and not score_board[p][ord(m) - 65]:
            failure_count[p][ord(m) - 65] += 1

#     failure_count
#     score_board

    answer = list()
    for i in range(1, P + 1):
        cnt = 0
        score = 0
        for j in range(M):
            if score_board[i][j]:
                cnt += 1
                score += score_board[i][j]
        answer.append((i, cnt, score))

    answer = sorted(answer, key = lambda x: (-x[1], x[2]))
#     answer
    print(f"Data Set {k}:")
    for a, b, c in answer:
        print(a, b, c)
    print()