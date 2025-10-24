import sys
input = sys.stdin.readline

t = int(input().rstrip())
for tc in range(1, t + 1):
    n = int(input().rstrip())
    t0, t1 = 2, 6
    
    if n == 0:
        ans = (t0 - 1) % 1000
    elif n == 1:
        ans = (t1 - 1) % 1000
    else:
        for _ in range(2, n + 1):
            t2 = (6 * t1 - 4 * t0) % 1000
            t0, t1 = t1, t2
        ans = (t1 - 1) % 1000
        
    print(f"Case #{tc}: {ans:03d}")