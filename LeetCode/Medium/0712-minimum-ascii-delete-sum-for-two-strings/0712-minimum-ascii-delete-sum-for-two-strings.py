class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        dy = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # 첫 열 초기화 (s1을 전부 삭제하는 경우)
        for i in range(1, n + 1):
            dy[i][0] = dy[i - 1][0] + ord(s1[i - 1])
        
        # 첫 행 초기화 (s2를 전부 삭제하는 경우)
        for i in range(1, m + 1):
            dy[0][i] = dy[0][i - 1] + ord(s2[i - 1])
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    # 같은 문자일 경우 이전 상태 그대로
                    dy[i][j] = dy[i - 1][j - 1]
                else:
                    # 문자가 다르면 둘 중 하나 삭제
                    dy[i][j] = min(
                        dy[i - 1][j] + ord(s1[i - 1]), # s1에서 삭제
                        dy[i][j - 1] + ord(s2[j - 1]) # s2에서 삭제
                    )
        
        return dy[n][m]