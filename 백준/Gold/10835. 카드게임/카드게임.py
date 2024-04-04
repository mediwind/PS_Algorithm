n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

# dy[i][j]는 왼쪽 카드 더미 0번 인덱스, 오른쪽 카드 더미 j번 인덱스부터 게임을 진행할 때 얻을 수 있는 최대 점수
dy = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        # 왼쪽 카드 버리기
        dy[i][j] = max(dy[i][j], dy[i+1][j])
        # 오른쪽 카드 버리기
        if left[i] > right[j]:
            dy[i][j] = max(dy[i][j], dy[i][j+1] + right[j])
        # 양쪽 카드 모두 버리기
        else:
            dy[i][j] = max(dy[i][j], dy[i+1][j+1])

print(dy[0][0])
