class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        count = 10  # n = 1일 때, 0부터 9까지 10개의 숫자가 있음
        unique_digits = 9  # 첫 번째 자리는 1~9 중 하나
        available_digits = 9  # 나머지 자리는 0~9 중 하나
        
        for i in range(1, n):
            unique_digits *= available_digits
            count += unique_digits
            available_digits -= 1
        
        return count