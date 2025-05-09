class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP 테이블 초기화
        dp = [0] * (amount + 1)
        dp[0] = 1  # 금액 0을 만드는 방법은 1가지 (아무 동전도 사용하지 않음)
        
        # 동전별로 DP 테이블 갱신
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]