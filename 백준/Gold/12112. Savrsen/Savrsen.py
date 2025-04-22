import math

MAX_N = 10_000_100

# 약수의 합 배열
sumDiv = [0 for _ in range((MAX_N + 2))]

"""에라토스테네스의 체를 사용하여 약수의 합 계산"""
for i in range(1, int(math.sqrt(MAX_N)) + 1):
    sumDiv[i * i] += i
    for j in range(i + 1, MAX_N // i + 1):
        sumDiv[i * j] += i + j

# 입력 처리
L, R = map(int, input().strip().split())

# 결과 계산
ans = 0
for i in range(L, R + 1):
    ans += abs(2 * i - sumDiv[i])

# 결과 출력
print(ans)