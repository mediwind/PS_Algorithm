def check(idx):
    for i in range(idx, -1, -1):
        if boxes[i] < boxes[idx]:
            dy[idx] = max(dy[idx], dy[i] + 1)


n = int(input())
boxes = list(map(int, input().split()))

dy = [1 for _ in range(n)]
for i in range(1, n):
    check(i)

print(max(dy))