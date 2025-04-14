def compute_gcd(a, b):
    """유클리드 호제법으로 최대공약수 계산"""
    while b:
        a, b = b, a % b
    return a


p = int(''.join(input().split('.')))  # 소수점 제거 후 정수로 변환
scale = 10 ** (len(str(p)) - 1)  # p와 같은 자릿수의 10의 거듭제곱
gcd_value = compute_gcd(p, scale)  # p와 scale의 최대공약수
p //= gcd_value  # 약분된 분자
scale //= gcd_value  # 약분된 분모

counts = [0] * 5  # 각 숫자(1~5)의 사용 횟수 저장
max_fives = (p - scale) // 4  # 5를 최대한 많이 사용
counts[4] += max_fives
p -= max_fives * 5
scale -= max_fives

if p != scale:  # 남은 차이를 다른 숫자로 채움
    counts[p - scale] += 1
    counts[0] += scale - 1
else:  # 남은 모든 값을 1로 채움
    counts[0] += scale

print(*counts)