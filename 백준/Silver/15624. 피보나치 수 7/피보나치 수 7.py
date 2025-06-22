MOD = 1000000007
n = int(input())

num1, num2 = 0, 1
res = 0
order = 2
while order <= n:
    res = (num1 + num2) % MOD
    num1 = num2
    num2 = res
    order += 1

print(res % MOD)