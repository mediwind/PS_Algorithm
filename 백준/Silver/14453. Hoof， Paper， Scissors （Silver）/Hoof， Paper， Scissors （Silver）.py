# 14453 Hoof, Paper, Scissors (Silver)
import sys
input = sys.stdin.readline

n = int(input().strip())

# prefix[H][i]는 i번째 게임까지 H가 '등장'한 수
prefix = [[0 for _ in range(n)] for _ in range(3)]
H, P, S = 0, 1, 2
h, p, s = 0, 0, 0
for i in range(n):
    ch = input().strip()
    if ch == 'H':
        h += 1
    elif ch == 'P':
        p += 1
    elif ch == 'S':
        s += 1
    prefix[H][i] = h
    prefix[P][i] = p
    prefix[S][i] = s

# i번째 게임을 기준으로 왼쪽(0부터 i까지)과 오른쪽(i+1부터 n-1까지)으로 나눕니다.
# max_left는 0부터 i까지의 게임에서 가장 많이 등장한 제스처의 횟수를 나타냅니다.
# max_right는 i+1부터 n-1까지의 게임에서 가장 많이 등장한 제스처의 횟수를 나타냅니다.
ans = 0
for i in range(n):
    max_left, max_right = 0, 0
    for j in range(3):
        max_left = max(max_left, prefix[j][i])
        max_right = max(max_right, prefix[j][n - 1] - prefix[j][i])
    ans = max(ans, max_left + max_right)

print(ans)