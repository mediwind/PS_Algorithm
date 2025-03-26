import sys
input = sys.stdin.readline

T = int(input().rstrip())
for t in range(1, T + 1):
    S = input().rstrip()
    n = len(S)

    ans = ""
    for i in range(n - 1, -1, -1):
        char = S[i]
        ans = min(char + ans, char * 2 + ans)

    print(f"Case #{t}: {ans}")