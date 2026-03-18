import sys
from decimal import Decimal
input = sys.stdin.readline

line = input().split()
if not line:
    sys.exit(0)

d = int(line[0])
p_dec = Decimal(line[1])
p_int = int(p_dec * Decimal('1000000000'))

prices = list(map(int, input().split()))

diff_sq_prefix = [0] * d
for i in range(1, d):
    diff = prices[i] - prices[i - 1]
    diff_sq_prefix[i] = diff_sq_prefix[i - 1] + diff * diff

p_sq = p_int * p_int
factor = 1000000000000000000 # 10^18
lhs_coeff = factor + p_sq

positive_count = 0
negative_count = 0

for i in range(d):
    for j in range(i + 2, d):
        n = j - i
        total_sum = prices[j] - prices[i]

        if total_sum == 0:
            continue

        total_sq = diff_sq_prefix[j] - diff_sq_prefix[i]

        lhs = lhs_coeff * (total_sum * total_sum)
        rhs = p_sq * n * total_sq

        if lhs >= rhs:
            if total_sum > 0:
                positive_count += 1
            else:
                negative_count += 1

print(f"{positive_count} {negative_count}")