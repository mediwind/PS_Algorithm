class Solution:
    def countVowelStrings(self, n: int) -> int:
# 중복조합을 사용
        return math.factorial(5 + n - 1) // (math.factorial(5 - 1) * math.factorial(n))