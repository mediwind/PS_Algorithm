import sys
import math
input = sys.stdin.readline

# 1. 네 변의 길이 입력 받기
line = input().split()
if not line:
    sys.exit()
a, b, c, d = map(int, line)

# 2. 둘레의 절반(semi-perimeter) s 계산
s = (a + b + c + d) / 2

# 3. 브라마굽타 공식을 이용해 최대 넓이 계산
max_area = math.sqrt((s - a) * (s - b) * (s - c) * (s - d))

print(max_area)