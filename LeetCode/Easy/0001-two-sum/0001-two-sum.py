class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()

        for idx, num in enumerate(nums):
            tmp = target - num
            if tmp not in table:
                table[num] = idx
            else:
                return [idx, table[tmp]]