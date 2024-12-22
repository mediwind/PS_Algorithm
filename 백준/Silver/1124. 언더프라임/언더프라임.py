from math import sqrt


def counting(x, primes):
    cnt = 0
    for prime in primes:
        if prime * prime > x:
            break
        while x % prime == 0:
            cnt += 1
            x //= prime
    
    if x != 1:
        cnt += 1
        
    return cnt


a, b = map(int, input().split())

nums = [True for _ in range(b + 1)]
nums[0] = nums[1] = False

for i in range(2, int(sqrt(b)) + 1):
    if nums[i]:
        for j in range(i * i, b + 1, i):
            nums[j] = False

primes = [i for i in range(2, b + 1) if nums[i]]

ans = 0
for i in range(a, b + 1):
    if nums[counting(i, primes)]:
        ans += 1

print(ans)