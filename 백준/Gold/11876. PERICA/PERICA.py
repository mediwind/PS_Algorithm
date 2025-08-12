def combinations(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k

    result = 1
    for i in range(k):
        result = (result * (n - i)) // (i + 1)
    return result


n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

MOD = 1000000007

total_sum = 0
for i in range(n):
    # a[i]가 최댓값이 되려면, a[i]보다 작은 값들 중에서 k-1개를 선택해야 함
    count = combinations(n - i - 1, k - 1)
    total_sum = (total_sum + a[i] * count) % MOD

print(total_sum)