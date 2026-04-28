class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        mod = grid[0][0] % x

        for row in grid:
            for col in row:
                if col % x != mod:
                    return -1
                nums.append(col)
                
        nums.sort()
        mid = nums[len(nums) >> 1]
        return sum(abs(col - mid) // x for col in nums)