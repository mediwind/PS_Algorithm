def repeat(s, n):
    return s * n


b, w = map(int, input().split())
z = max(b, w)

r = 4
c = z * 2

print(r, c)
print(repeat(".@", w - 1) + repeat("@@", z - w + 1))
print(repeat("@@", z))
print(repeat("..", z))
print(repeat(".@", b - 1) + repeat("..", z - b + 1))