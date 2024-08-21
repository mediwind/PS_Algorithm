def solve(N, M, hole, dotori):
    Where = [0 for _ in range(N + 1)]
    fin = 0
    for i in range(1, N + 1):
        if hole[i][0] <= fin:
            continue
        if Where[N] != 0:
            break
        for j in range(fin, min(hole[i][0], N) + 1):
            if Where[j] == 0:
                Where[j] = hole[i][1]
        fin = hole[i][0]
    
    ans = list()
    for i in range(1, M + 1):
        ans.append(Where[dotori[i]])
    print(" ".join(map(str, ans)))


N = int(input())
holes = list(map(int, input().split()))
hole = [(0, 0) for _ in range(N + 1)]
for i in range(1, N + 1):
    hole[i] = (holes[i - 1] + (i - 1), i)

M = int(input())
dotori = [0 for _ in range(M + 1)]
acorns = list(map(int, input().split()))
for i in range(1, M + 1):
    dotori[i] = acorns[i - 1]

solve(N, M, hole, dotori)