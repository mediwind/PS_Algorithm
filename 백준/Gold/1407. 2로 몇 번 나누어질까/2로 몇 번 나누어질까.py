def f(x):
    ret = 0
    i = 1
    while x > 0:
        if x & 1:
            y = x // 2 + 1
        else:
            y = x // 2
        ret += y * i
        x -= y
        i *= 2
    return ret


a, b = map(int, input().split())
print(f(b) - f(a - 1))