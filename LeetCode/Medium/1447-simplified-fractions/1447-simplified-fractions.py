class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # 단순 분수(simplified fractions)는  분자와 분모가 서로소인 분수
        answer = list()
        for d in range(2, n + 1):
            for num in range(1, d):
                if math.gcd(num, d) == 1:
                    answer.append(f"{num}/{d}")
        
        return answer