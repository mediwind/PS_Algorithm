from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        distance = [float('inf') for _ in range(n)]
        distance[0] = 0

        Q = deque()
        Q.append((0, nums[0], 0))
        while Q:
            idx, reach, dist = Q.popleft()
            for i in range(idx + 1, idx + reach + 1):
                if i >= n:
                    break
                if distance[i] == float('inf'):
                    distance[i] = dist + 1
                    Q.append((i, nums[i], dist + 1))
        print(dist)

        return distance[-1]