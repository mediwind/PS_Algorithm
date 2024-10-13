n = int(input())

colors = [0 for _ in range(n + 1)]
colors[1] = 1
color_count = 1

for i in range(2, n + 1):
    if colors[i] != 0:
        continue

    color_count += 1
    num = i

    while num <= n:
        colors[num] = color_count
        num += i

print(color_count)
print(' '.join(map(str, colors[1:])))