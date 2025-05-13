dy = [0 for _ in range(70)]
dy[0] = dy[1] = 1
dy[2] = 2
dy[3] = 4

for i in range(4, 70):
    dy[i] = sum(dy[i - 4:i])

t = int(input())
for _ in range(t):
    n = int(input())
    print(dy[n])