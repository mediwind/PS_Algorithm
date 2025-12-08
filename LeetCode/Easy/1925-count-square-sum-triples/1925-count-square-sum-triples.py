class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(2, int(n ** 0.5) + 1):
            for j in range(1, i):
                if i - j & 1 == 0 or gcd(i, j) != 1:
                    continue
                cnt = i * i + j * j
                if cnt > n:
                    continue
                
                ans += 2 * (n // cnt)
        
        return ans