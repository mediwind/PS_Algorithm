class Solution:
    def maxWalls(self, robots, distance, walls):
        import bisect
        
        robots_with_dist = sorted(zip(robots, distance))
        robots = [r for r, _ in robots_with_dist]
        distance = [d for _, d in robots_with_dist]

        walls.sort()

        n = len(robots)

        left = [0] * n
        right = [0] * n
        overlap = [0] * n

        for i in range(n):
            r = robots[i]
            d = distance[i]

            pos_r = bisect.bisect_right(walls, r)

            if i > 0:
                left_bound = max(r - d, robots[i - 1] + 1)
            else:
                left_bound = r - d

            left_pos = bisect.bisect_left(walls, left_bound)
            left[i] = pos_r - left_pos

            if i < n - 1:
                right_bound = min(r + d, robots[i + 1] - 1)
            else:
                right_bound = r + d

            right_pos = bisect.bisect_right(walls, right_bound)
            pos_l = bisect.bisect_left(walls, r)

            right[i] = right_pos - pos_l

            if i > 0:
                prev_robot_pos = bisect.bisect_left(walls, robots[i - 1])
                overlap[i] = pos_r - prev_robot_pos

        dp_left = left[0]
        dp_right = right[0]

        for i in range(1, n):
            new_left = max(
                dp_left + left[i],
                dp_right - right[i - 1] + min(left[i] + right[i - 1], overlap[i]),
            )

            new_right = max(
                dp_left + right[i],
                dp_right + right[i],
            )

            dp_left, dp_right = new_left, new_right

        return max(dp_left, dp_right)