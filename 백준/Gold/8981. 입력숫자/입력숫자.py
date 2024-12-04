n = int(input())
arr = list(map(int, input().split()))
x = [-1] * n

print(n)
x[0] = arr[0]
cur = 0
for i in range(1, n):
    value = x[cur]
    cur = (cur + value) % n
    while x[cur] != -1:
        cur = (cur + 1) % n
    x[cur] = arr[i]

for i in range(n):
    print(x[i], end=' ')