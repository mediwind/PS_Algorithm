import sys
input = sys.stdin.readline

MOD = 1000000007

T = int(input().strip())
for _ in range(T):
    p, q, r = map(int, input().split())
    ans = (min(q, r) + (p - 1)) % MOD
    print(ans)