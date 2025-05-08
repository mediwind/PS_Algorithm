class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 메모이제이션을 위한 캐시
        memo = {}

        # Helper 함수: 주어진 수식에 대해 가능한 결과를 계산
        def compute(expr):
            # 이미 계산된 결과가 있다면 캐시에서 반환
            if expr in memo:
                return memo[expr]
            
            # 결과를 저장할 리스트
            results = []

            # 수식에서 연산자를 기준으로 분할
            for i, char in enumerate(expr):
                if char in "+-*":  # 연산자 발견
                    # 왼쪽과 오른쪽 부분을 재귀적으로 계산
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])

                    # 왼쪽과 오른쪽 결과를 조합하여 계산
                    for left in left_results:
                        for right in right_results:
                            if char == "+":
                                results.append(left + right)
                            elif char == "-":
                                results.append(left - right)
                            elif char == "*":
                                results.append(left * right)

            # 연산자가 없는 경우 (숫자만 있는 경우)
            if not results:
                results.append(int(expr))

            # 결과를 캐시에 저장
            memo[expr] = results
            return results

        # 전체 수식에 대해 계산
        return compute(expression)