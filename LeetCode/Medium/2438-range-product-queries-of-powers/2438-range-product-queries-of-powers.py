class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        powers = []
        i = 0
        temp = n
        while temp > 0:
            if temp % 2 == 1:
                powers.append(2 ** i)
            temp //= 2
            i += 1

        prefix = [1]
        for p in powers:
            prefix.append((prefix[-1] * p) % MOD)

        res = []
        for l, r in queries:
            prod = (prefix[r+1] * pow(prefix[l], MOD-2, MOD)) % MOD
            res.append(prod)

        return res