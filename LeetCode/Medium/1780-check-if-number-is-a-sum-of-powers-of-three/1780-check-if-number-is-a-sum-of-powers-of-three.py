class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # n을 3진수로 검사: 자리값이 2가 나오면 불가능
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True