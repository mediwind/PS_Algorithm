n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

# 하드 드라이브를 모두 0으로 초기화
hard_drive = ['0'] * n

# 고장난 비트를 '0'으로 설정
for i in range(b):
    broken_bits[i] -= 1

# 주어진 논리에 따라 하드 드라이브를 채움
for i in range(b):
    start = broken_bits[i - 1] + 1 if i > 0 else 1 if c % 2 == 0 else 0
    for j in range(start, broken_bits[i], 2):
        if c > 0:
            hard_drive[j] = '1'
            c -= 2

# 리스트를 결합하여 최종 비트 문자열 생성
result = ''.join(hard_drive)
print(result)