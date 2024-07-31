import sys
input = sys.stdin.readline

# 입력받기
n, m = map(int, input().split())

# 2차원 리스트(matrix) 입력받기
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 각 행의 합을 저장할 리스트
row_sums = [0] * n
# 각 열의 합을 저장할 리스트
col_sums = [0] * m

# 각 행의 합 계산
for i in range(n):
    for j in range(m):
        row_sums[i] += matrix[i][j]

# 각 열의 합 계산
for j in range(m):
    for i in range(n):
        col_sums[j] += matrix[i][j]

# 최대 값을 저장할 변수
max_sum = float('-inf')

# 가능한 모든 사각형의 합 계산
for i in range(n):
    for j in range(m):
        for k in range(i + 1, n):
            for l in range(j + 1, m):
                # 사각형의 합 계산
                current_sum = row_sums[i] + col_sums[j] + row_sums[k] + col_sums[l] \
                              - matrix[i][j] - matrix[k][l] - matrix[i][l] - matrix[k][j] \
                              + (k - i - 1) * (l - j - 1)

                # 최대 값 갱신
                max_sum = max(max_sum, current_sum)

# 결과 출력
print(max_sum)