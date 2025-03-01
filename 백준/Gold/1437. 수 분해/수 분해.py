import sys

n = int(input())
if n == 0 or n == 1:
    print(n)
    sys.exit(0)

mx = n // 3
re = n % 3
ans = 1

if re == 2:
    ans *= 2
elif re == 1:
    ans *= 4
    mx -= 1

for _ in range(mx):
    ans *= 3
    ans %= 10007

print(ans)