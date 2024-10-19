n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        # 0이 아닌 색을 만난 경우
        if board[i][j] > 0:
            # 그 색을 저장한 후
            color = board[i][j]
            # 그 색을 만난 지점부터 그 지점의 가로 끝까지 탐색
            for k in range(j, m):
                # 0을 만나는 경우 break
                if board[i][k] == 0:
                    break
                # 같은 색을 만났다면 이미 칠했다는 의미로 0으로 처리
                elif board[i][k] == color:
                    board[i][k] = 0
            
            cnt += 1

print(cnt)