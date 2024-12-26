import math

INF = 10**7
is_prime = [True for _ in range(INF)]
is_prime[0] = is_prime[1] = False

for number in range(2, int(math.sqrt(INF)) + 1):
    if is_prime[number]:
        for multiple in range(number * number, INF, number):
            is_prime[multiple] = False

primes = [num for num in range(2, INF) if is_prime[num]]
k = int(input())
print(primes[k - 1])