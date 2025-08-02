class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        
        k = n // m
        
        divisible = m * k * (k + 1) // 2
        not_divisible = total - divisible
        return not_divisible - divisible  