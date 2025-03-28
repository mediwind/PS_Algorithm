class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP 테이블 생성
        dy = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dy[0][0] = True  # 빈 문자열과 빈 패턴은 매칭됨

        # '*'가 0개 이상의 이전 요소를 매칭할 수 있는 경우 처리
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dy[0][j] = dy[0][j - 2]

        # DP 테이블 채우기
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dy[i][j] = dy[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dy[i][j] = dy[i][j - 2] or (dy[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return dy[len(s)][len(p)]