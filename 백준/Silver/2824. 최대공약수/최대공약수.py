def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
xs = list(map(int, input().split()))
res_1 = 1
for x in xs:
    res_1 *= x

m = int(input())
ys = list(map(int, input().split()))
res_2 = 1
for y in ys:
    res_2 *= y

ans = gcd(res_1, res_2)
ans = str(ans)[-9:]
print(ans)