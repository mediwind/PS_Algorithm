import sys
input = sys.stdin.readline


def get_divisors(x, limit):
    divisors = set()
    d = 1
    while d * d <= x:
        if x % d == 0:
            if d <= limit:
                divisors.add(d)
            other = x // d
            if other <= limit:
                divisors.add(other)
        d += 1
    return divisors


n = int(input().strip())
months = list(map(int, input().strip().split()))

limit = min(months) // 4

unique_months = list(set(months))

answer = 0

if len(unique_months) <= 3:
    answer = limit * (limit + 1) // 2
    print(answer)
    sys.exit()

u = unique_months[:4]
candidates = set()

for i in range(4):
    for j in range(i + 1, 4):
        diff = abs(u[i] - u[j])
        if diff > 0:
            candidates.update(get_divisors(diff, limit))

for L in candidates:
    remainders = set()
    possible = True
    
    for days in unique_months:
        remainders.add(days % L)
        if len(remainders) > 3:
            possible = False
            break
            
    if possible:
        answer += L

print(answer)