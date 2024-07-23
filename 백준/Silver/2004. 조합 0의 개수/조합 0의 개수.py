def two_count(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += n
    return cnt


def five_count(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt


n, m = map(int, input().split())

a = two_count(n) - two_count(n - m) - two_count(m)
b = five_count(n) - five_count(n - m) - five_count(m)
ans = min(a, b)
print(ans)