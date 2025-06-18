import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 각 매장별 최고 매출액, 최고 직원
best_sale = [0 for _ in range(M + 1)]
best_emp = [0 for _ in range(M + 1)]
# 각 직원별 최고 매장 수
cnt = [0 for _ in range(N + 1)]
# 각 직원-매장별 매출
board = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for emp in range(1, N + 1):
    data = list(map(int, input().split()))
    for i in range(0, K * 2, 2):
        store, sale = data[i], data[i + 1]
        board[emp][store] = sale
        if sale > best_sale[store]:
            best_sale[store] = sale
            best_emp[store] = emp

for store in range(1, M + 1):
    if best_emp[store]:
        cnt[best_emp[store]] += 1

# 영업왕 수 미리 계산
num_king = sum(1 for x in cnt[1:] if x == K)

Q = int(input())
for _ in range(Q):
    i, j, v = map(int, input().split())
    prev_emp = best_emp[j]
    board[i][j] += v
    if board[i][j] > best_sale[j]:
        # 영업왕 수 갱신
        if cnt[prev_emp] == K:
            num_king -= 1
        cnt[prev_emp] -= 1
        best_sale[j] = board[i][j]
        best_emp[j] = i
        cnt[i] += 1
        if cnt[i] == K:
            num_king += 1
    elif i == best_emp[j]:
        best_sale[j] = board[i][j]
    print(num_king)