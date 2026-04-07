import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())

stars = [tuple(map(int, input().split())) for _ in range(k)]

max_caught = 0

for x1, _ in stars:
    for _, y1 in stars:
        count = 0

        x2 = x1 + l
        y2 = y1 + l

        for x, y in stars:
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1

        max_caught = max(max_caught, count)

print(k - max_caught)