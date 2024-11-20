arr = list(map(int, input().split()))
x, y, r = map(int, input().split())

ans = 0
for i in range(4):
    if x == arr[i]:
        ans = i + 1

print(ans)