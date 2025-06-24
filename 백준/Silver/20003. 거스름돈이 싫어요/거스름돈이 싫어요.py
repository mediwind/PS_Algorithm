def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a


def LCM(a, b):
    res = a * b // GCD(a, b)
    return res


N = int(input())
fractions = [tuple(map(int, input().split())) for _ in range(N)]

# 1. 모든 분수의 공통분모 구하기
denoms = [b for a, b in fractions]
common_den = denoms[0]
for d in denoms[1:]:
    common_den = LCM(common_den, d)

# 2. 공통분모로 통분한 분자들 구하기
numerators = list()
for a, b in fractions:
    numerators.append(a * (common_den // b))

# 3. 분자들의 GCD 구하기
num_gcd = numerators[0]
for n in numerators[1:]:
    num_gcd = GCD(num_gcd, n)

# 4. 분자와 분모를 다시 한 번 약분
final_gcd = GCD(num_gcd, common_den)
print(f"{num_gcd // final_gcd} {common_den // final_gcd}")