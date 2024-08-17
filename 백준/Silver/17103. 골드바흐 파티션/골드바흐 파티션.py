import sys

primes = []
is_composite = [0] * 1000001
is_composite[0] = 1
is_composite[1] = 1

# Sieve of Eratosthenes to find all prime numbers up to 1,000,000
for i in range(2, 1000001):
    if is_composite[i] == 0:
        primes.append(i)
        for j in range(2 * i, 1000001, i):
            is_composite[j] = 1

T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for prime in primes:
        if prime >= N:
            break
        if not is_composite[N - prime] and prime <= N - prime:  # Avoid counting permutations
            count += 1
    print(count)