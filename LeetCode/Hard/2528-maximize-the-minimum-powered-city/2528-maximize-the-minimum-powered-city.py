from itertools import accumulate

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        base = [0] * (n + 5)
        for idx, val in enumerate(stations):
            base[max(0, idx - r)] += val
            base[min(n - 1, idx + r) + 1] -= val
        left, right = min(accumulate(base[:n])), 2 * 10**10
        
        def feasible(target):
            cur_diff = base[:]
            running = 0
            used = 0
            for i in range(n):
                running += cur_diff[i]

                if running < target:
                    need = target - running
                    used += need
                    cur_diff[min(n - 1, i + 2 * r) + 1] -= need
                    running = target

                if used > k:
                    return False

            return True

        while left < right:
            m = (left + right + 1) >> 1
            if feasible(m):
                left = m
            else:
                right = m - 1

        return left