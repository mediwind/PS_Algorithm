import math


def is_prime(number):  # Check if a number is prime
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


N = int(input())
palindrome_prime = 0

for num in range(N, 1000001):  # Iterate from input number N to the maximum value
    if num == 1:  # 1 is not a prime number, so skip it
        continue
    if str(num) == str(num)[::-1]:  # Check if the number is a palindrome
        if is_prime(num):  # Check if the palindrome number is prime
            palindrome_prime = num
            break

if palindrome_prime == 0:  # If no palindrome prime is found within the range
    palindrome_prime = 1003001  # The smallest palindrome prime greater than 1,000,000

print(palindrome_prime)