# n을 k진수로 변환
def into_k_digit(n, k):
    res = []
    while n:
        res.append(n % k)
        n //= k
    return ''.join(map(str, res[::-1]))


# 소수 판별
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    k_base_number = into_k_digit(n, k)
    candidates = k_base_number.split('0')
    
    prime_count = 0
    for candidate in candidates:
        if candidate and is_prime(int(candidate)):
            prime_count += 1
    
    return prime_count