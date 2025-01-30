import sys
input = sys.stdin.readline


def calculate_distance(a, b):
    if a <= b:
        return prefix_sum[b] - prefix_sum[a]
    else:
        return prefix_sum[n] - prefix_sum[a] + prefix_sum[b]


n = int(input())
arr = [int(input()) for _ in range(n)]
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]

ans = float("-inf")
lt, rt = 0, 1
while lt < n:
    res1 = calculate_distance(lt, rt)
    res2 = prefix_sum[n] - res1
    ans = max(ans, min(res1, res2))
    
    if res1 < res2:
        rt = (rt + 1) % n
        if rt == 0:
            break
    else:
        lt += 1
        if lt == rt:
            rt = (rt + 1) % n
            if rt == 0:
                break

print(ans)