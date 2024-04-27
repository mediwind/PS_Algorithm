N = int(input())
dy = [[[0]*2 for _ in range(3)] for _ in range(N+1)]
dy[1][0][0] = 1
dy[1][1][0] = 1
dy[1][0][1] = 1
divNum = 1_000_000

for i in range(2, N+1):
    dy[i][0][0] = (dy[i-1][0][0] + dy[i-1][1][0] + dy[i-1][2][0]) % divNum
    dy[i][0][1] = (dy[i-1][0][0] + dy[i-1][1][0] + dy[i-1][2][0] + dy[i-1][0][1] + dy[i-1][1][1] + dy[i-1][2][1]) % divNum
    dy[i][1][0] = dy[i-1][0][0] % divNum
    dy[i][1][1] = dy[i-1][0][1] % divNum
    dy[i][2][0] = dy[i-1][1][0] % divNum
    dy[i][2][1] = dy[i-1][1][1] % divNum

answer = (dy[N][0][0] + dy[N][0][1] + dy[N][1][0] + dy[N][1][1] + dy[N][2][0] + dy[N][2][1]) % divNum
print(answer)