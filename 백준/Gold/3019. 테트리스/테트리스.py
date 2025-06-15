c, p = map(int, input().split())
floor = list(map(int, input().split()))
ans = 0

if p == 1:
    ans += c
    for i in range(3, c):
        if floor[i - 3] == floor[i - 2] and floor[i - 3] == floor[i - 1] and floor[i - 3] == floor[i]:
            ans += 1
elif p == 2:
    for i in range(1, c):
        if floor[i - 1] == floor[i]:
            ans += 1
elif p == 3:
    for i in range(2, c):
        if floor[i - 2] == floor[i - 1] and floor[i - 1] == floor[i] - 1:
            ans += 1
        if floor[i - 1] - 1 == floor[i]:
            ans += 1
    if floor[0] - 1 == floor[1]:
        ans += 1
elif p == 4:
    for i in range(2, c):
        if floor[i - 2] - 1 == floor[i - 1] and floor[i - 1] == floor[i]:
            ans += 1
        if floor[i - 1] == floor[i] - 1:
            ans += 1
    if floor[0] == floor[1] - 1:
        ans += 1
elif p == 5:
    for i in range(2, c):
        if floor[i - 2] == floor[i - 1] and floor[i - 2] == floor[i]:
            ans += 1
        if floor[i - 2] - 1 == floor[i - 1]:
            ans += 1
        if floor[i - 1] == floor[i] - 1:
            ans += 1
        if floor[i - 2] - 1 == floor[i - 1] and floor[i - 1] == floor[i] - 1:
            ans += 1
elif p == 6:
    for i in range(1, c):
        if floor[i - 1] == floor[i]:
            ans += 1
        if i >= 2 and floor[i - 2] == floor[i - 1] and floor[i - 2] == floor[i]:
            ans += 1
        if i >= 2 and floor[i - 2] == floor[i - 1] - 1 and floor[i - 1] == floor[i]:
            ans += 1
        if floor[i - 1] - 2 == floor[i]:
            ans += 1
elif p == 7:
    for i in range(1, c):
        if floor[i - 1] == floor[i]:
            ans += 1
        if i >= 2 and floor[i - 2] == floor[i - 1] and floor[i - 2] == floor[i]:
            ans += 1
        if i >= 2 and floor[i - 2] == floor[i - 1] and floor[i - 1] - 1 == floor[i]:
            ans += 1
        if floor[i - 1] == floor[i] - 2:
            ans += 1

print(ans)