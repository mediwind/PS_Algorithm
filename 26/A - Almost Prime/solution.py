import sys
input = sys.stdin.readline
 
n = int(input().strip())
 
prime_factor_count = [0] * (n + 1)
 
for i in range(2, n + 1):
    if prime_factor_count[i] == 0:  # i가 소수인 경우
        for j in range(i, n + 1, i):
            prime_factor_count[j] += 1
 
ans = 0
for i in range(1, n + 1):
    if prime_factor_count[i] == 2:
        ans += 1
 
print(ans)