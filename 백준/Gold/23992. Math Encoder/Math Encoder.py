def ensure_pow2(length):
    while len(pow2) <= length:
        pow2.append((pow2[-1] * 2) % MOD)

MOD = 1_000_000_007

pow2 = [1]

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    ensure_pow2(N)
    result = 0
    for i, val in enumerate(nums):
        contrib = (pow2[i] - pow2[N - 1 - i]) % MOD
        result = (result + val * contrib) % MOD
        
    print(f"Case #{case}: {result}")