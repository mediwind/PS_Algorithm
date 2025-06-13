class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def can_make_pairs(max_diff):
            count = 0
            i = 0
            n = len(nums)
            while i < n - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # use both indices
                else:
                    i += 1
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if can_make_pairs(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer