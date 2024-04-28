class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = list()
        n, m = len(matrix), len(matrix[0])
        lt, rt = 0, m
        top, bottom = 0, n

        while lt < rt and top < bottom:
            for i in range(lt, rt):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                ans.append(matrix[i][rt - 1])
            rt -= 1

            if not(lt < rt and top < bottom):
                break
            
            for i in range(rt - 1, lt - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][lt])
            lt += 1
        
        return ans