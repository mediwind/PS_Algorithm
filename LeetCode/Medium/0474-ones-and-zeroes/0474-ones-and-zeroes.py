class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j]는 "최대 i개의 0과 최대 j개의 1을 사용하여 만들 수 있는 부분 집합의 최대 크기"
        dy = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dy[i][j] = max(dy[i][j], dy[i - zeros][j - ones] + 1)
        
        return dy[m][n]