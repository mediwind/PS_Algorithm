import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))

basis = [0] * 61

for x in a:
    for i in range(60, -1, -1):
        if (x >> i) & 1:
            if not basis[i]:
                basis[i] = x
                break
            x ^= basis[i]

max_xor = 0
for i in range(60, -1, -1):
    if (max_xor ^ basis[i]) > max_xor:
        max_xor ^= basis[i]

print(max_xor)