class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dy = [[1], [1, 1]]

        if rowIndex <= 1:
            return dy[rowIndex]
        
        for i in range(2, rowIndex + 1): # 2 ~ 4: 2, 3
            tmp = list()
            for j in range(i - 1): # 3 - 1: 0, 1
                tmp.append(dy[i - 1][j] + dy[i - 1][j + 1])
            tmp = [1] + tmp + [1]
            dy.append(tmp)
        
        return dy[rowIndex]