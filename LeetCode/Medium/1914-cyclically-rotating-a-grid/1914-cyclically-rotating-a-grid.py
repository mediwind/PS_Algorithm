class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):
            top = left = layer
            bottom = m - 1 - layer
            right = n - 1 - layer

            arr = []

            # extract
            for j in range(left, right + 1):
                arr.append(grid[top][j])

            for i in range(top + 1, bottom):
                arr.append(grid[i][right])

            for j in range(right, left - 1, -1):
                arr.append(grid[bottom][j])

            for i in range(bottom - 1, top, -1):
                arr.append(grid[i][left])

            # rotate
            kk = k % len(arr)
            arr = arr[kk:] + arr[:kk]

            idx = 0

            # write back
            for j in range(left, right + 1):
                grid[top][j] = arr[idx]
                idx += 1

            for i in range(top + 1, bottom):
                grid[i][right] = arr[idx]
                idx += 1

            for j in range(right, left - 1, -1):
                grid[bottom][j] = arr[idx]
                idx += 1

            for i in range(bottom - 1, top, -1):
                grid[i][left] = arr[idx]
                idx += 1

        return grid