import sys
input = sys.stdin.readline

line = input().split()
if not line:
    sys.exit(0)
N, P = map(int, line)

T = list(map(int, input().split()))

if N > 1:
    K = list(map(int, input().split()))

ans = sum(T) + (P - 1) * max(T)
print(ans)