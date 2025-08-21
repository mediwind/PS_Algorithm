import math
import sys
# input = sys.stdin.readline


def divisors(n):
    ds = set()
    r = int(math.isqrt(n))
    for i in range(1, r+1):
        if n % i == 0:
            ds.add(i)
            ds.add(n//i)
    return ds


def weekday_divisors(n):
    return sorted(d for d in divisors(n) if d > 1 and (d % 7 == 1 or d % 7 == 6))


while True:
    
    try:
        line = input().rstrip()
    except EOFError:
        break
        
    if not line:
        continue
        
    n = int(line)
    
    if n == 1:
        break
        
    wd = weekday_divisors(n)
    primitive = list()
    seen = list()
    for d in wd:
        is_prime_wd = True
        for e in seen:
            if d % e == 0:
                is_prime_wd = False
                break
        if is_prime_wd:
            primitive.append(d)
        seen.append(d)
        
    print(f"{n}: " + (" ".join(map(str, primitive)) if primitive else ""))