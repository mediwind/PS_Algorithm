def xor_upto(n):
    m = n % 4
    if m == 0:
        return n
    elif m == 1:
        return 1
    elif m == 2:
        return n + 1
    else:
        return 0


A, B = map(int, input().split())
result = xor_upto(A - 1) ^ xor_upto(B)
print(result)