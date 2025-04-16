def base_conversion(a, b, digits):
    # A진법 -> 10진법 변환
    decimal_value = 0
    for i, digit in enumerate(reversed(digits)):
        decimal_value += digit * (a ** i)

    # 10진법 -> B진법 변환
    if decimal_value == 0:
        return [0]
    
    b_base_digits = []
    while decimal_value > 0:
        b_base_digits.append(decimal_value % b)
        decimal_value //= b

    return b_base_digits[::-1]  # 높은 자릿수부터 출력


a, b = map(int, input().split())  # A진법과 B진법
m = int(input())  # 자리수
digits = list(map(int, input().split()))  # A진법 숫자의 각 자리값

result = base_conversion(a, b, digits)
print(*result)