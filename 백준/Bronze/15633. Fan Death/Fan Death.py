n = int(input())

ans = 0
for i in range(1, n + 1):
    if not n % i:
        ans += i

print(ans * 5 - 24)