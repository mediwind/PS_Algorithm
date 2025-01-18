X, K = map(int, input().split())

Y = 0
bit_position = 0
while K > 0:
    if (X & (1 << bit_position)) == 0:
        if (K & 1) == 1:
            Y |= (1 << bit_position)
        K >>= 1
    bit_position += 1

print(Y)