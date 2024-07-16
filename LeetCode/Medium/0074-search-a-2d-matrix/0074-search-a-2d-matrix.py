class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        arr = list()
        for i in range(n):
            arr += matrix[i]
        
        lt, rt = 0, (n * m) - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if arr[mid] == target:
                return True
            
            if arr[mid] < target:
                lt = mid + 1
            else:
                rt = mid - 1

        return False