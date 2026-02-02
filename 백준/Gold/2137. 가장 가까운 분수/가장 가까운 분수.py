import math

a, b = map(int, input().split())

MAX = 32767

best_x = 0
best_y = 1
best_num = None
best_den = None

for y in range(1, MAX + 1):
    t = a * y // b

    for x in (t, t + 1):
        if x <= 0 or x >= y:
            continue
        if x == a and y == b:
            continue
        if math.gcd(x, y) != 1:
            continue

        num = abs(a * y - b * x)
        den = b * y

        if best_num is None:
            best_num = num
            best_den = den
            best_x, best_y = x, y
        else:
            if num * best_den < best_num * den:
                best_num = num
                best_den = den
                best_x, best_y = x, y
            elif num * best_den == best_num * den:
                if x * best_y < best_x * y:
                    best_x, best_y = x, y

print(best_x, best_y)