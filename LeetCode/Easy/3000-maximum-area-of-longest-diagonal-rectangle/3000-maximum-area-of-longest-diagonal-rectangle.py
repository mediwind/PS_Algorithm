class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # 대각선 길이의 제곱을 비교해서 sqrt 없이 결정
        max_diag_sq = -1
        max_area = 0
        
        for l, w in dimensions:
            diag_sq = l*l + w*w
            area = l*w
            if diag_sq > max_diag_sq or (diag_sq == max_diag_sq and area > max_area):
                max_diag_sq = diag_sq
                max_area = area

        return max_area