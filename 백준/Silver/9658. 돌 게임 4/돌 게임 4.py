n = int(input())
dy = [0 for _ in range(1001)]
dy[2] = dy[4] = 1

for i in range(5, n + 1):
    if not dy[i - 1] or not dy[i - 3] or not dy[i - 4]:
        dy[i] = 1

if dy[n]:
    print("SK")
else:
    print("CY")