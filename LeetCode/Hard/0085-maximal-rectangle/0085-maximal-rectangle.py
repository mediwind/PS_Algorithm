class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0 for _ in range(cols)]  # 누적 높이를 저장하는 배열
        max_area = 0  # 최대 직사각형 면적
        
        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # 히스토그램의 최대 면적 구하기
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 히스토그램에서 최대 직사각형 면적 계산
        stack = list()
        max_area = 0
        heights.append(0)  # Stack이 언제 어떻게 빌지 모르므로 Sentinel 역할의 0을 추가
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        heights.pop()  # sentinel을 마저 제거
        return max_area