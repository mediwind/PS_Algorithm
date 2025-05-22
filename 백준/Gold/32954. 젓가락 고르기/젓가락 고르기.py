import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 0:
    print(0)
    sys.exit(0)

s_val = 0
p_val = 0
for count in A:
    if count >= 1: # 각 색깔의 젓가락은 최소 1개
        s_val += (count - 1) // 2
        p_val += (count - 1) % 2

max_possible_pairs = s_val + p_val

if K > max_possible_pairs:
    print(-1)
    sys.exit(0)

if K <= s_val:
    result = N + 2 * K - 1
    print(result)
else:
    result = N + 2 * s_val + (K - s_val)
    print(result)