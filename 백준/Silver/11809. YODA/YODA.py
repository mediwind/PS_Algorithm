n_str = input().strip()
m_str = input().strip()

# 두 문자열의 최대 길이를 구함
max_len = max(len(n_str), len(m_str))

# 길이가 짧은 문자열 앞에 0을 채워 길이를 맞춤
n_str = n_str.zfill(max_len)
m_str = m_str.zfill(max_len)

# 결과를 저장할 리스트 초기화
result_n_digits = list()
result_m_digits = list()

# 각 자리수를 비교
for i in range(max_len):
    digit_n = int(n_str[i])
    digit_m = int(m_str[i])

    if digit_n > digit_m:
        # N의 숫자가 더 크면 N의 결과 리스트에 추가
        result_n_digits.append(n_str[i])
    elif digit_m > digit_n:
        # M의 숫자가 더 크면 M의 결과 리스트에 추가
        result_m_digits.append(m_str[i])
    else: # digit_n == digit_m
        # 숫자가 같으면 양쪽 결과 리스트에 모두 추가
        result_n_digits.append(n_str[i])
        result_m_digits.append(m_str[i])

# 최종 결과 처리
# N의 결과 리스트가 비어있으면 "YODA"
if not result_n_digits:
    result_n = "YODA"
else:
    # 그렇지 않으면 리스트의 숫자들을 합쳐 정수로 변환
    # int()는 자동으로 앞의 0을 제거해줌 (예: int("005") -> 5)
    result_n = int("".join(result_n_digits))

# M의 결과 리스트가 비어있으면 "YODA"
if not result_m_digits:
    result_m = "YODA"
else:
    # 그렇지 않으면 리스트의 숫자들을 합쳐 정수로 변환
    result_m = int("".join(result_m_digits))

# 결과 출력
print(result_n)
print(result_m)