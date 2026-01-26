import sys
input = sys.stdin.readline

N = int(input())
prime_sums = {}

for _ in range(N):
    num = int((input()))
    original_val = num

    if num == 1:
        continue

    d = 2
    temp = num

    while d * d <= temp:
        if temp % d == 0:
            prime_sums[d] = prime_sums.get(d, 0) + original_val

            while temp % d == 0:
                temp //= d
        d += 1

    if temp > 1:
        prime_sums[temp] = prime_sums.get(temp, 0) + original_val

if not prime_sums:
    print(0)
else:
    print(max(prime_sums.values()))