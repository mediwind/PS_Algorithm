import sys
input = sys.stdin.readline

MAX_VAL = 1000000
values = [1] * (MAX_VAL + 1)
values[1] = 0
cum_sum = 0
for length in range(2, 1414):
    cum_sum += length - 1
    mult = 2
    while length * mult + cum_sum <= MAX_VAL:
        values[length * mult + cum_sum] += 1
        mult += 1

while True:
    q = int(input().strip())
    if q == 0:
        break
    print(values[q])