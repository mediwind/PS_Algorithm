import sys
# input = sys.stdin.readline

MOD = 10 ** 9 + 7

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().rstrip().split())
    S = input().rstrip()

    half = (N + 1) // 2
    prefix = 0
    for i in range(half):
        prefix = prefix * K + (ord(S[i]) - ord('a'))
    ans = prefix

    pal = S[:half]
    if N % 2 == 0:
        pal += pal[::-1]
    else:
        pal += pal[:-1][::-1]

    pal_str = ''.join(pal)
    if pal_str < S:
        ans += 1

    ans %= MOD
    print(f"Case #{t}: {ans}")