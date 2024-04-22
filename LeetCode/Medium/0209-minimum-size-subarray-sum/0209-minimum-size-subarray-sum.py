class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        lt, rt = 0, 0
        total = nums[0]
        answer = float('inf')
        while lt <= rt:
            if total < target:
                rt += 1
                if rt >= n:
                    break
                total += nums[rt]
            else:
                answer = min(answer, rt - lt + 1)
                total -= nums[lt]
                lt += 1
            # print(lt, rt, total, answer)

        if answer == float('inf'):
            return 0

        return answer