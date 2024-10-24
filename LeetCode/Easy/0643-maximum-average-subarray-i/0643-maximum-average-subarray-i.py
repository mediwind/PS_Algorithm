class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        lt, rt = 0, k - 1
        tmp = sum(nums[lt:rt + 1])
        res = [tmp]
        while True:
            tmp -= nums[lt]
            lt += 1
            rt += 1
            if lt > n - k or rt > n - 1:
                break
            tmp += nums[rt]
            res.append(tmp)
            
        return max(res) / k