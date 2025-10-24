class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        from itertools import permutations

        nums = set()
        for mask in range(1, 1<<9):
            digits = []
            total = 0
            for d in range(1,10):
                if mask >> (d-1) & 1:
                    digits += [str(d)] * d
                    total += d

            if 1 <= total <= 7:
                for perm in set(permutations(digits)):
                    nums.add(int(''.join(perm)))

        arr = sorted(nums)

        for v in arr:
            if v > n:
                return v

        return -1