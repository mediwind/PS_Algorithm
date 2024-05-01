MOD = 1_000_000_000
n = int(input())

dy = [0] * (n + 1)
dy[0] = 1

power = 1
while power <= n:
    for i in range(power, n + 1):
        dy[i] = (dy[i] + dy[i - power]) % MOD
    power *= 2

print(dy[n])