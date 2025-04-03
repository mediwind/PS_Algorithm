import math
import sys

a, b = map(int, input().split())

# 예외 처리: 영식이가 먹는 분량이 0이면 민식이만 먹음
if a == 0:
    print("-")
    sys.exit(0)

# 영식이가 전부 먹는 경우
if a == b:
    print("*")
    sys.exit(0)

# L: 패턴의 길이 (1 <= L <= 60)
for L in range(1, 61):
    total = (2 ** L) - 1  # 한 패턴에서 분모가 되는 값
    # (total * a)가 b로 나누어 떨어져 정수가 되는지 확인
    if (total * a) % b == 0:
        t = (total * a) // b  # 패턴을 2진수로 해석한 값
        # 2진수 변환: 길이가 L이 안되면 왼쪽에 0을 붙인다.
        bin_str = format(t, 'b').zfill(L)
        # 2진수를 '*' (영식)와 '-' (민식)으로 치환
        pattern = bin_str.replace('1', '*').replace('0', '-')
        print(pattern)
        sys.exit(0)

# 길이가 60 이하인 패턴이 없으면 -1 출력
print(-1)