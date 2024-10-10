from itertools import permutations


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


test_cases = int(input())
for _ in range(test_cases):
    prime_count = 0
    input_string = input().strip()
    digits = [int(char) for char in input_string]
    unique_numbers = set()
    
    for length in range(1, len(digits) + 1):
        for perm in permutations(digits, length):
            num = int(''.join(map(str, perm)))
            unique_numbers.add(num)
    
    for num in unique_numbers:
        if is_prime(num):
            prime_count += 1
    
    print(prime_count)