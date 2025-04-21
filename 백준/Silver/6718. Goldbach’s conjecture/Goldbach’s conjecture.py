import math
import sys
input = sys.stdin.readline


def is_prime(num):
    """소수 판별 함수"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def count_goldbach_pairs(n, primes):
    """골드바흐의 추측에 따라 소수 쌍의 개수를 계산"""
    count = 0
    for p in primes:
        if p > n // 2:
            break
        if n - p in primes_set:
            count += 1
    return count


# 에라토스테네스의 체로 소수 리스트 생성
numbers = list()
while True:
    n = int(input().strip())
    if n == 0:
        break
    numbers.append(n)

max_n = max(numbers)
sieve = [True for _ in range(max_n + 1)]
sieve[0] = sieve[1] = False
for i in range(2, int(math.sqrt(max_n)) + 1):
    if sieve[i]:
        for j in range(i * i, max_n + 1, i):
            sieve[j] = False

primes = [i for i in range(max_n + 1) if sieve[i]]
primes_set = set(primes)

for n in numbers:
    result = count_goldbach_pairs(n, primes)
    print(result)