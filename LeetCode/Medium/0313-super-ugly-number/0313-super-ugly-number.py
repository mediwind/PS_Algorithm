class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        idx = [0 for _ in range(k)]
        uglies = [1]
        for _ in range(1, n):
            candidates = [uglies[idx[j]] * primes[j] for j in range(k)]
            next_ugly = min(candidates)
            uglies.append(next_ugly)
            for j in range(k):
                if candidates[j] == next_ugly:
                    idx[j] += 1
                    
        return uglies[-1]