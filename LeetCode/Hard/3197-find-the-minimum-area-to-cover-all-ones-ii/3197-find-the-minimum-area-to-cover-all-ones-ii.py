class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        INF = float("inf")
        ans = INF
        # 4가지 방향(0,90,180,270도) 모두 시도
        for _ in range(4):
            n, m = len(grid), len(grid[0])
            # 첫 번째 가로 절단 위치 i
            for i in range(1, n):
                area_top = self.boundingArea(grid[:i])  # 위쪽 블록의 최소 사각형 넓이
                # 아래 블록을 세로로 절단하는 경우
                for j in range(1, m):
                    bl = [row[:j] for row in grid[i:]]   # 아래-왼쪽
                    br = [row[j:] for row in grid[i:]]   # 아래-오른쪽
                    area_bl = self.boundingArea(bl)
                    area_br = self.boundingArea(br)
                    total = area_top + area_bl + area_br
                    if total < ans:
                        ans = total
                # 아래 블록을 다시 가로로 절단하는 경우
                for i2 in range(i + 1, n):
                    mid = grid[i:i2]
                    bot = grid[i2:]
                    area_mid = self.boundingArea(mid)
                    area_bot = self.boundingArea(bot)
                    total = area_top + area_mid + area_bot
                    if total < ans:
                        ans = total
            # 90도 회전해서 다른 방향도 동일하게 검사
            grid = self.rotate90(grid)
        return ans

    def boundingArea(self, A: List[List[int]]) -> int:
        # A 내부의 1들을 모두 포함하는 최소 bounding box의 넓이 (1이 없으면 0)
        if not A or not A[0]:
            return 0
        n, m = len(A), len(A[0])
        left, right = m, -1
        top, bottom = n, -1
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    if j < left: left = j
                    if j > right: right = j
                    if i < top: top = i
                    if i > bottom: bottom = i
        if right == -1:
            return 0
        return (right - left + 1) * (bottom - top + 1)

    def rotate90(self, A: List[List[int]]) -> List[List[int]]:
        # 90도 시계 회전 (행렬 크기 m x n 으로 반환)
        n, m = len(A), len(A[0])
        return [[A[n-1-i][j] for i in range(n)] for j in range(m)]