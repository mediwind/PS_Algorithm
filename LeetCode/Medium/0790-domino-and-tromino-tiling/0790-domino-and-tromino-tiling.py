class Solution:
    def numTilings(self, n):
        dy = [[0, 0] for _ in range(3)]
        dy[1], dy[2] = [1, 1], [2, 2]
        for i in range(3, n+1):
            dy[i%3][0] = dy[(i-1)%3][0] + dy[(i-2)%3][0] + 2*dy[(i-2)%3][1]
            dy[i%3][1] = dy[(i-1)%3][0] + dy[(i-1)%3][1]
        return dy[n%3][0] % 1_000_000_007