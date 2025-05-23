N = int(input())
blocks = list(input())

dy = [float("inf") for _ in range(N)]
dy[0] = 0

chain = {
    "B": "J",
    "O": "B",
    "J": "O"
}

for i in range(1, N):
    now_block = blocks[i]
    for j in range(i):
        prev_block = blocks[j]
        
        if chain[now_block] == prev_block:
            cost = (j - i) ** 2
            if dy[i] > dy[j] + cost:
                dy[i] = dy[j] + cost

if dy[N - 1] == float("inf"):
    print(-1)
else:
    print(dy[N - 1])