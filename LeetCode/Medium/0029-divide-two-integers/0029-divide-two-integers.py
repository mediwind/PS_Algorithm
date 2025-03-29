class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 상수 정의: 32비트 정수 범위
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # 예외 처리: 나눗셈 결과가 범위를 벗어나는 경우
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # 부호 결정
        negative = (dividend < 0) != (divisor < 0)

        # 절댓값으로 변환
        dividend, divisor = abs(dividend), abs(divisor)

        # 결과 계산
        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # 부호 적용
        if negative:
            quotient = -quotient

        # 결과 반환
        return max(INT_MIN, min(INT_MAX, quotient))