class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # 1이 있는 좌표를 추출
        def get_ones_positions(img):
            positions = []
            for i in range(n):
                for j in range(n):
                    if img[i][j] == 1:
                        positions.append((i, j))
            return positions
        
        # img1과 img2에서 1이 있는 좌표를 가져옴
        ones_img1 = get_ones_positions(img1)
        ones_img2 = get_ones_positions(img2)
        
        # 벡터 이동을 기록할 Counter
        vector_count = Counter()
        
        # 모든 좌표 쌍에 대해 벡터 이동 계산
        for x1, y1 in ones_img1:
            for x2, y2 in ones_img2:
                vector = (x2 - x1, y2 - y1)
                vector_count[vector] += 1
        
        # 가장 많이 겹친 벡터의 값 반환
        return max(vector_count.values(), default=0)