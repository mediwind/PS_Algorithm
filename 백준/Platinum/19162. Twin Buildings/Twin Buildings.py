import sys
input = sys.stdin.readline

n = int(input().strip())

lands = []
ans_x2 = 0

for _ in range(n):
    l, w = map(int, input().split())
    s = min(l, w)
    t = max(l, w)

    lands.append((s, t))

    ans_x2 = max(ans_x2, s * t)

lands.sort(reverse=True)

best_long = 0

for s, t in lands:
    if best_long > 0:
        ans_x2 = max(ans_x2, 2 * s * min(t, best_long))
        
    best_long = max(best_long, t)

print(f"{ans_x2 // 2}.{ans_x2 % 2 * 5}")