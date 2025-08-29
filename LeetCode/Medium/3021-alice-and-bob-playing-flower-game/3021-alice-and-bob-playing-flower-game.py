class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Alice가 승리하려면 한 레인의 꽃의 수는 홀수, 다른 레인의 꽃의 수는 짝수여야 한다.
        return n * m // 2