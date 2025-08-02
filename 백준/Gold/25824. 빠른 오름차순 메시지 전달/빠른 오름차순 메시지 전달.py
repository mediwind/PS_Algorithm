time_matrix = [list(map(int, input().split())) for _ in range(12)]

# 그룹: (첫번째 학생의 인덱스, 두번째 학생의 인덱스)
groups = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]

# 2^6 = 64가지 경우의 수 (각 그룹별 주문 결정)
min_total = float("inf")
for mask in range(1 << 6):
    total = 0
    # 그룹0: 선생님으로부터 받은 메시지는 즉시 전달되어 전송 시간은 0.
    # 그룹0에서는 옵션에 따라 학생 순서를 결정한다.
    g0_first, g0_second = groups[0]
    if mask & 1:
        # 옵션 B: 순서 (g0_second, g0_first)
        total += time_matrix[g0_second][g0_first]
        last_student = g0_first
    else:
        # 옵션 A: 순서 (g0_first, g0_second)
        total += time_matrix[g0_first][g0_second]
        last_student = g0_second

    # 그룹1부터 그룹5까지 차례대로 메시지 전달
    for i in range(1, 6):
        a, b = groups[i]
        if (mask >> i) & 1:
            # 옵션 B: 현재 그룹의 순서 (b, a)
            total += time_matrix[last_student][b] + time_matrix[b][a]
            last_student = a
        else:
            # 옵션 A: 현재 그룹의 순서 (a, b)
            total += time_matrix[last_student][a] + time_matrix[a][b]
            last_student = b

    if total < min_total:
        min_total = total

print(min_total)