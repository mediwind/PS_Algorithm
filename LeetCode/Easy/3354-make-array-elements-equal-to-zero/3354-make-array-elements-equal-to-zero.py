class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        ans = 0
        for i, val in enumerate(nums):

            if val != 0:
                continue

            left = prefix[i]
            right = total - prefix[i + 1]

            if right == left or right == left + 1:
                ans += 1

            if left == right or left == right + 1:
                ans += 1
                
        return ans