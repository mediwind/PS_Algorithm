from math import gcd
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    base = nums[0]
    g = 0
    all_same = True
    for x in nums[1:]:
        if x != base:
            all_same = False
        g = gcd(g, abs(x - base))
    if all_same:
        print("INFINITY")
    else:
        print(g)