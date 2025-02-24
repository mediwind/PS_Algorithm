class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [1 for _ in range(n)]
        is_prime[0] = is_prime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for i in range(i * i, n, i):
                    is_prime[i] = 0
        
        return sum(is_prime)