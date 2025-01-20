m = int(input())
x2 = 0

if m == 1:
    print(1, 1)
    exit()

# 문제 A: M을 가능한 한 큰 수의 곱으로 분해
t = m
x1 = (t + 2) // 3

# 문제 B: M을 가능한 한 작은 수의 합으로 분해
while m % 4 == 0:
    m //= 4
    x2 += 1
for i in range(2, 1000001):
    while m % i == 0:
        m //= i
        x2 += 1

print(x1, x2)