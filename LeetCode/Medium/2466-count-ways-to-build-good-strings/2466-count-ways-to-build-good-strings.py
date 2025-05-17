class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        
        # dy[i]는 길이가 i인 문자열을 만드는 방법의 수
        dy = [0 for _ in range(high + 1)]
        dy[0] = 1

        for i in range(1, high + 1):
            if i - zero >= 0:
                dy[i] = (dy[i] + dy[i - zero]) % MOD
            if i - one >= 0:
                dy[i] = (dy[i] + dy[i - one]) % MOD
        
        return sum(dy[low:high + 1]) % MOD
