n, m = map(int, input().split())

not_capitals = set()
for _ in range(m):
    a, b = map(int, input().split())
    not_capitals.add(b)

capitals = []
for i in range(1, n + 1):
    if i not in not_capitals:
        capitals.append(i)

print(len(capitals))
for capital in capitals:
    print(capital)