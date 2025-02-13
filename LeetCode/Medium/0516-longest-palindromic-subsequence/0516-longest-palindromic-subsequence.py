class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp 배열 초기화
        dy = [[0 for _ in range(n)] for _ in range(n)]

        # 길이가 1인 부분 문자열 초기화
        for i in range(n):
            dy[i][i] = 1
        
        # 길이가 2 이상인 부분 문자열 처리
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                # 양 끝 문자가 같은 경우
                if s[start] == s[end]:
                    dy[start][end] = dy[start + 1][end - 1] + 2
                # 양 끝 문자가 다른 경우
                else:
                    dy[start][end] = max(dy[start + 1][end], dy[start][end - 1])
        
        return dy[0][n - 1]