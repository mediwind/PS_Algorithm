a, b, c = sorted(map(int, input().split()))

if a + 2 == c:
    print(0)
elif a + 2 == b or b + 2 == c:
    print(1)
else:
    print(2)

print(max(b - a, c - b) - 1)