class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        def modinv(x):
            return pow(x, MOD - 2, MOD)

        # 팩토리얼과 역팩토리얼 미리 계산
        fact = [1 for _ in range(n)]
        inv_fact = [1 for _ in range(n)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[n-1] = modinv(fact[n - 1])
        for i in range(n - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        ways = comb(n - 1, k) * m % MOD
        ways = ways * pow(m - 1, n - k - 1, MOD) % MOD
        return ways