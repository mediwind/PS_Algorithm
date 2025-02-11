class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 각 숫자의 등장 횟수를 카운트
        count = Counter(nums)
        nums = sorted(list(set(nums)))  # 중복 제거 및 정렬
        
        # DP 배열 초기화
        n = len(nums)
        dp = [0] * (n + 1)
        
        # 첫 번째 숫자는 무조건 선택 가능
        if n >= 1:
            dp[0] = nums[0] * count[nums[0]]
        
        # 두 번째 숫자부터 처리
        if n >= 2:
            # 첫 번째와 두 번째 숫자가 연속적이지 않은 경우
            if nums[1] - nums[0] > 1:
                dp[1] = dp[0] + nums[1] * count[nums[1]]
            else:
                dp[1] = max(dp[0], nums[1] * count[nums[1]])
        
        # 나머지 숫자들 처리
        for i in range(2, n):
            # 현재 숫자와 이전 숫자가 연속적이지 않은 경우
            if nums[i] - nums[i-1] > 1:
                dp[i] = dp[i-1] + nums[i] * count[nums[i]]
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i] * count[nums[i]])
        
        return dp[n-1] if n > 0 else 0