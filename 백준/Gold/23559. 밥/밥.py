import sys
input = sys.stdin.readline

N, X = map(int, input().rstrip().split())

meals = list()
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    meals.append((a, b, a - b))

meals.sort(key = lambda x: (-x[2]))

ans = 0
for i in range(N):
    a, b, diff = meals[i]
    if diff < 0:
        ans += b
        X -= 1000
    else:
        if ((N - 1) - i) * 1000 <= X - 5000:
            ans += a
            X -= 5000
        else:
            ans += b
            X -= 1000

print(ans)