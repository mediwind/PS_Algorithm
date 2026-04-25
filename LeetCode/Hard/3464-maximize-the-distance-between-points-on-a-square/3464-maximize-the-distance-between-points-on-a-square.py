class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        from bisect import bisect_left

        perimeter = 4 * side

        def to_pos(x: int, y: int) -> int:
            if x == 0:
                return y
            if y == side:
                return side + x
            if x == side:
                return 3 * side - y
            return 4 * side - x

        def manhattan(a_idx: int, b_idx: int) -> int:
            x1, y1 = ordered[a_idx][1], ordered[a_idx][2]
            x2, y2 = ordered[b_idx][1], ordered[b_idx][2]
            return abs(x1 - x2) + abs(y1 - y2)

        ordered = []
        for x, y in points:
            ordered.append((to_pos(x, y), x, y))
        ordered.sort()

        n = len(ordered)
        pos = [p for p, _, _ in ordered]

        extended_pos = pos + [p + perimeter for p in pos]

        def can_make(dist: int) -> bool:
            nxt = [0] * (2 * n)
            j = 0
            for i in range(2 * n):
                if j < i + 1:
                    j = i + 1
                while j < 2 * n and extended_pos[j] - extended_pos[i] < dist:
                    j += 1
                nxt[i] = j

            LOG = k.bit_length() + 1

            jump = [nxt[:]]
            for _ in range(LOG):
                prev = jump[-1]
                cur = [2 * n] * (2 * n)
                for i in range(2 * n):
                    if prev[i] < 2 * n:
                        cur[i] = prev[prev[i]]
                jump.append(cur)

            for start in range(n):
                cur = start
                need = k - 1

                bit = 0
                while need:
                    if need & 1:
                        cur = jump[bit][cur]
                        if cur >= start + n:
                            break
                    need >>= 1
                    bit += 1
                else:
                    if cur < start + n and manhattan(cur % n, start) >= dist:
                        return True

            return False

        lo, hi = 0, side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_make(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo