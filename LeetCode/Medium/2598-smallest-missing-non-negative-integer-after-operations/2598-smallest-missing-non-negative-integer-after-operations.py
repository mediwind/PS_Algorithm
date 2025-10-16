class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for a in nums:
            cnt[a % value] += 1
            
        x = 0
        while True:
            r = x % value
            if cnt[r] > 0:
                cnt[r] -= 1
                x += 1
            else:
                return x