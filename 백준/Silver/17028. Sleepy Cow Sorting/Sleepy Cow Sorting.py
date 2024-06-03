N = int(input())
cows = list(map(int, input().split()))
ans = N - 1
for i in range(N - 2, -1, -1):
    if cows[i] < cows[i + 1]:
        ans = i
    else:
        break

print(ans)