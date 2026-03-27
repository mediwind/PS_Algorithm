class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n

        for i in range(m):
            row = mat[i]
            if i % 2 == 0:
                shifted = row[k:] + row[:k]
            else:
                shifted = row[-k:] + row[:-k]

            if shifted != row:
                return False

        return True