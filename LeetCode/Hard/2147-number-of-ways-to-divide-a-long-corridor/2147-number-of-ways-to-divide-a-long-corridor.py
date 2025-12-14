class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']

        m = len(seats)
        if m == 0 or m % 2 == 1:
            return 0
        if m == 2:
            return 1

        ways = 1
        pairs = m // 2
        for k in range(1, pairs):
            ways = (ways * (seats[2*k] - seats[2*k - 1])) % MOD
            
        return ways