class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_size = 0
        left = 0

        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1

            max_size = max(max_size, right - left + 1)

        return n - max_size