class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # pow2[i]는 2의 i제곱(2^i) 값을 의미
        # l~`r` 사이의 원소들로 만들 수 있는 부분수열(서브시퀀스)의 개수는 2^(r-l)개
        #(최소값 nums[l]과 최대값 nums[r]는 반드시 포함, 나머지 원소는 포함/미포함 선택 가능)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD

        res = 0
        l, r = 0, n - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + pow2[r - l]) % MOD
                l += 1
            else:
                r -= 1
                
        return res