n = int(input())

mod = 987654321
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, n + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, n + 1) if is_prime[i]]

result = 1
for prime in primes:
    if prime > n:
        break
    k = prime
    while k * prime <= n:
        k *= prime
    result = (result * k) % mod

print(result)