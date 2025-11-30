class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0

        prefix_mod_map = {0: -1}
        n = len(nums)
        current = 0
        min_len = n
        for i, x in enumerate(nums):
            current = (current + x) % p
            need = (current - remainder) % p
            if need in prefix_mod_map:
                min_len = min(min_len, i - prefix_mod_map[need])
            prefix_mod_map[current] = i
            
        return min_len if min_len < n else -1