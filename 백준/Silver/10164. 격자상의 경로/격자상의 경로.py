def get_val(n, m, k, dy):
    # k가 0이면, 그리드의 오른쪽 아래 모서리의 값을 반환
    if k == 0:
        return dy[n][m]
    
    # k번째 셀의 좌표 (ax, ay) 계산
    ax = k // m + (1 if k % m > 0 else 0)
    ay = k - (ax - 1) * m
    
    # (ax, ay)에서 오른쪽 아래 모서리까지의 셀 좌표 (bx, by) 계산
    bx = n - ax + 1
    by = m - ay + 1
    
    # (ax, ay)와 (bx, by)에서의 값의 곱을 반환
    return dy[ax][ay] * dy[bx][by]

# n, m, k 입력값 읽기
n, m, k = map(int, input().split())

# (n+1) x (m+1) 크기의 2D 리스트 (dy)를 0으로 초기화
dy = [[0] * (m + 1) for _ in range(n + 1)]

# 시작점 값 설정
dy[0][1] = 1

# 각 셀에 도달하는 방법의 수로 2D 리스트 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dy[i][j] = dy[i - 1][j] + dy[i][j - 1]

# get_val 함수의 결과 출력
print(get_val(n, m, k, dy))