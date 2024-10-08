import math

# 입력을 받습니다.
n = int(input())

# n이 제곱수인 경우 -1을 출력하고 종료합니다.
if math.isqrt(n) ** 2 == n:
    print(-1)
else:
    ans = set()

    # n이 제곱수가 아닌 경우
    # 1. 길이가 √n인 변이 빗변인 경우
    for i in range(1, math.isqrt(n) + 1):
        x = i
        y = math.sqrt(n - x * x)
        if y.is_integer():
            y = int(y)
            if x > y:
                x, y = y, x
            ans.add((x, y))

    # 2. 길이가 √n인 변이 빗변이 아닌 경우
    divisors = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    divisors.sort()
    for i in range((len(divisors) + 1) // 2):
        if divisors[i] % 2 == divisors[-i - 1] % 2:
            ans.add((divisors[i], divisors[-i - 1]))

    # 정답 출력
    print(len(ans))