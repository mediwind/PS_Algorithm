class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]

        Q = [1]
        ch = set()
        ch.add(1)

        for _ in range(n):
            ugly = heapq.heappop(Q)

            for prime in primes:
                new_ugly = ugly * prime
                if new_ugly not in ch:
                    ch.add(new_ugly)
                    heapq.heappush(Q, new_ugly)
        
        return ugly