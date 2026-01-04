class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        import math

        def factor(n: int):
            res = []
            temp = n
            for p in primes:
                if p * p > temp:
                    break
                    
                if temp % p == 0:
                    e = 0
                    while temp % p == 0:
                        temp //= p
                        e += 1
                    res.append((p, e))

                if temp == 1:
                    break

            if temp > 1:
                res.append((temp, 1))

            return res

        if not nums:
            return 0

        mx = max(nums)
        lim = int(math.isqrt(mx)) + 1
        sieve = [True] * (lim + 1)
        primes = []
        for i in range(2, lim + 1):
            if sieve[i]:
                primes.append(i)
                for j in range(i * i, lim + 1, i):
                    sieve[j] = False

        total = 0
        for x in nums:
            if x <= 1:
                continue

            fac = factor(x)
            cnt_div = 1
            for _, e in fac:
                cnt_div *= (e + 1)

            if cnt_div != 4:
                continue

            sigma = 1
            for p, e in fac:
                sigma *= (p ** (e + 1) - 1) // (p - 1)
            total += sigma

        return total