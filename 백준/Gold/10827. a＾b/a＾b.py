def calculate_power_with_decimal(a_str, b_str):
    # 입력을 소수와 정수로 변환
    decimal_places = len(a_str) - 1 - a_str.find('.')
    a_parts = a_str.split('.')
    a_int = int(a_parts[0] + a_parts[1])
    b = int(b_str)

    # b를 이진수로 변환
    b_bin = bin(b)[2:]

    # 제곱 계산
    result = a_int
    for i in range(1, len(b_bin)):
        result *= result
        if b_bin[i] == '1':
            result *= a_int

    # 결과를 문자열로 변환하여 소수점 삽입
    result_str = str(result)
    while len(result_str) < decimal_places * b + 1:
        result_str = '0' + result_str

    front = result_str[:len(result_str) - decimal_places * b]
    back = result_str[len(result_str) - decimal_places * b:]
    
    return front + '.' + back


# 입력 받기
a, b = input().split()

# 결과 계산 및 출력
result = calculate_power_with_decimal(a, b)
print(result)