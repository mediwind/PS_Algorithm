class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        lt, rt = 0, n - 1
        while lt < rt:
            tmp = numbers[lt] + numbers[rt]
            if tmp == target:
                return [lt + 1, rt + 1]
            elif tmp < target:
                lt += 1
            else:
                rt -= 1