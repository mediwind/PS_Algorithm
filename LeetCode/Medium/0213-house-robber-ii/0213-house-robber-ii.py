class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_simulation(arr):
            n = len(arr)
            
            if n == 1:
                return arr[0]
            if n == 2:
                return max(arr)
            
            dp = [0 for _ in range(n)]
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
            
            return dp[-1]
        
        '''
        이 문제는 원형이기 때문에,
        첫 번째 집과 마지막 집을 동시에 털 수 없습니다.
        '''

        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # 첫 집을 털지 않는 경우: nums[1:]만 고려
        res_1 = rob_simulation(nums[1:])
        # 마지막 집을 털지 않는 경우: nums[:-1]만 고려
        res_2 = rob_simulation(nums[:-1])

        return max(res_1, res_2)