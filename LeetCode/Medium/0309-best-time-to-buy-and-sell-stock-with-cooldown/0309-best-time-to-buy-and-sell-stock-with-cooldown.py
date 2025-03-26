class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        hold, sell, cooldown = -prices[0], 0, 0  # 초기값 설정
        
        for i in range(1, n):
            prev_hold, prev_sell, prev_cooldown = hold, sell, cooldown
            
            # 상태 업데이트
            hold = max(prev_hold, prev_cooldown - prices[i])  # 주식을 사거나 유지
            sell = prev_hold + prices[i]  # 주식을 판매
            cooldown = max(prev_cooldown, prev_sell)  # 쿨다운 유지
        
        # 최종 결과는 주식을 보유하지 않은 상태에서의 최대 이익
        return max(sell, cooldown)