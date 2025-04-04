import sys
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

for i in range(2, int(MAX**0.5) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * 2, MAX + 1, i):
        is_prime[j] = False

count = 0
for i in range(2, MAX + 1):
    if not is_prime[i]:
        continue
    if i % K == 1:
        print(i, end=" ")
        count += 1
        if count == N:
            break