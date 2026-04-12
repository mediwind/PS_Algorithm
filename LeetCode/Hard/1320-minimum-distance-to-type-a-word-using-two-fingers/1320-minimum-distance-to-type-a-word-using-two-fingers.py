class Solution:
    def minimumDistance(self, word: str) -> int:
        # 거리 계산
        def get_dist(x, y):
            if x == -1 or y == -1:
                return 0
            x1, y1 = divmod(x, 6)
            x2, y2 = divmod(y, 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        INF = float('inf')
        
        # dp[left][right]
        dp = [[INF] * 26 for _ in range(26)]
        
        first = ord(word[0]) - ord('A')
        
        # 초기 상태: 한 손만 사용
        for i in range(26):
            dp[first][i] = 0
            dp[i][first] = 0
        
        # DP 진행
        for i in range(1, n):
            cur = ord(word[i]) - ord('A')
            prev = ord(word[i-1]) - ord('A')
            
            new_dp = [[INF] * 26 for _ in range(26)]
            
            for l in range(26):
                for r in range(26):
                    if dp[l][r] == INF:
                        continue
                    
                    # 1. 왼손 이동
                    new_dp[cur][r] = min(
                        new_dp[cur][r],
                        dp[l][r] + get_dist(l, cur)
                    )
                    
                    # 2. 오른손 이동
                    new_dp[l][cur] = min(
                        new_dp[l][cur],
                        dp[l][r] + get_dist(r, cur)
                    )
            
            dp = new_dp
        
        # 결과
        return min(min(row) for row in dp)