class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutations = itertools.permutations

        arr = list(range(1, n + 1))
        order = 0
        for perm in permutations(arr, n):
            order += 1
            if order == k:
                return ''.join(map(str, perm))