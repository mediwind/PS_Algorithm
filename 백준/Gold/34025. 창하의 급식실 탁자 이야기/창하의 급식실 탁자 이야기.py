import sys
input = sys.stdin.readline

n = int(input().strip())

base_cols = 0
count_ones = 0
count_odd_gt1 = 0

for _ in range(n):
    a = int(input().strip())
    base_cols += (a + 1) // 2
    if a == 1:
        count_ones += 1
    elif a & 1:
        count_odd_gt1 += 1

if n == 1:
    # base_cols already minimal
    print(base_cols)
else:
    if count_odd_gt1 > 0:
        max_tight = count_ones + (count_odd_gt1 // 2)
    else:
        max_tight = max(0, count_ones - 1)

    answer = base_cols + (n - 1) - max_tight
    print(answer)