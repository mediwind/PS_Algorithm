class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(values, length) -> bool:
            for idx in range(1, length):
                if values[idx] < values[idx - 1]:
                    return False
            return True

        operation_count = 0
        length = len(nums)

        while not is_sorted(nums, length):
            operation_count += 1
            min_pair_sum = float("inf")
            min_pos = -1

            for idx in range(1, length):
                pair_sum = nums[idx - 1] + nums[idx]
                if pair_sum < min_pair_sum:
                    min_pair_sum = pair_sum
                    min_pos = idx

            nums[min_pos - 1] = min_pair_sum
            for idx in range(min_pos, length - 1):
                nums[idx] = nums[idx + 1]

            length -= 1

        return operation_count