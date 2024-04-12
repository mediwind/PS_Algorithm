import sys
input = sys.stdin.readline

def what_color(color):
    # 색을 바꿀 곳을 1로 표시하기
    change_board = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not (i + j)%2:
                if board[i][j] != color:
                    change_board[i][j] = 1
            else:
                if board[i][j] == color:
                    change_board[i][j] = 1
    
    # 2. 누적합 구하기
    prefix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = change_board[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
    res = prefix_sum
    
    # 3. res[0][0]부터 res[n-1][n-1]까지 k 간격으로 이동하며 최소 구간합 찾기
    answer = float('inf')
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            answer = min(answer, res[i + k - 1][j + k - 1] - res[i + k - 1][j - 1] - res[i - 1][j + k - 1] + res[i - 1][j - 1])
    
    return answer

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 1. 시작하는 컬러 [0][0]이 어떤 색일때 다시 칠하는 횟수가 적을까
black = what_color('B')
white = what_color('W')

print(min(black, white))