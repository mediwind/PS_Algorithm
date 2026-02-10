class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        ch = [0] * (max(nums) + 1)

        for i in range(n):
            if n - i <= ans:
                break

            arr = [0, 0]
            
            for j in range(i, n):
                val = nums[j]
                if ch[val] != i + 1:
                    ch[val] = i + 1
                    arr[val & 1] += 1

                if arr[0] == arr[1]:
                    ans = max(ans, j - i + 1)

        return ans