class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dy = [[1], [1, 1]]

        if numRows <= 2:
            return dy[:numRows]
        
        for i in range(3, numRows + 1):
            tmp = [1 for _ in range(i)]
            for j in range(1, i - 1):
                tmp[j] = dy[-1][j - 1] + dy[-1][j]
            dy.append(tmp)
        
        return dy