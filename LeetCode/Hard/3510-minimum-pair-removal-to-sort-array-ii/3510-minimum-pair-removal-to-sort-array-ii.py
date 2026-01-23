class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return 0

        values = [int(x) for x in nums]
        is_removed = [False] * length
        pair_heap = []
        increasing_count = 0

        for idx in range(1, length):
            heapq.heappush(pair_heap, (values[idx - 1] + values[idx], idx - 1))
            if values[idx] >= values[idx - 1]:
                increasing_count += 1

        if increasing_count == length - 1:
            return 0

        remaining = length
        prev_index = [i - 1 for i in range(length)]
        next_index = [i + 1 for i in range(length)]

        while remaining > 1:
            if not pair_heap:
                break

            pair_sum, left_idx = heapq.heappop(pair_heap)
            right_idx = next_index[left_idx]

            if (
                right_idx >= length
                or is_removed[left_idx]
                or is_removed[right_idx]
                or values[left_idx] + values[right_idx] != pair_sum
            ):
                continue

            prev_idx = prev_index[left_idx]
            next_idx = next_index[right_idx]

            if values[left_idx] <= values[right_idx]:
                increasing_count -= 1
            if prev_idx != -1 and values[prev_idx] <= values[left_idx]:
                increasing_count -= 1
            if next_idx != length and values[right_idx] <= values[next_idx]:
                increasing_count -= 1

            values[left_idx] += values[right_idx]
            is_removed[right_idx] = True
            remaining -= 1

            if prev_idx != -1:
                heapq.heappush(pair_heap, (values[prev_idx] + values[left_idx], prev_idx))
                if values[prev_idx] <= values[left_idx]:
                    increasing_count += 1
            else:
                prev_index[left_idx] = -1

            if next_idx != length:
                prev_index[next_idx] = left_idx
                next_index[left_idx] = next_idx
                heapq.heappush(pair_heap, (values[left_idx] + values[next_idx], left_idx))
                if values[left_idx] <= values[next_idx]:
                    increasing_count += 1
            else:
                next_index[left_idx] = length

            if increasing_count == remaining - 1:
                return length - remaining

        return length