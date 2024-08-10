class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dy = [amount + 1] * (amount + 1)
        dy[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dy[a] = min(dy[a], 1 + dy[a - c])
        
        return dy[amount] if dy[amount] != amount + 1 else -1