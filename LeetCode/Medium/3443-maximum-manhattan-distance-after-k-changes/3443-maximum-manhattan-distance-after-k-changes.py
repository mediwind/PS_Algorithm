class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def calc_max_dist(s: str, k: int, directions: str) -> int:
            max_dist = 0
            curr_pos = 0
            change_count = 0

            for move in s:
                if move in directions:
                    curr_pos += 1
                else:
                    curr_pos -= 1
                    change_count += 1
                max_dist = max(max_dist, curr_pos + 2 * min(k, change_count))

            return max_dist

        return max(
            calc_max_dist(s, k, 'NE'),
            calc_max_dist(s, k, 'NW'),
            calc_max_dist(s, k, 'SE'),
            calc_max_dist(s, k, 'SW')
        )