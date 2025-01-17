num_primes = int(input())
primes = list(map(int, input().split()))
max_value = int(input())

total_sum = 0
for prime in primes:
    count = 0
    current_value = max_value
    while current_value > 1:
        count += (current_value // prime)
        current_value //= prime
    total_sum += count

print(total_sum)