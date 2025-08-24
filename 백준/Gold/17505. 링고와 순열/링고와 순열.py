N, K = map(int, input().split())

max_inv = N * (N - 1) // 2
if K < 0 or K > max_inv:
    print(-1)
else:
    l, r = 1, N
    ans = list()
    while l <= r:
        if K >= (r - l):
            ans.append(r)
            K -= (r - l)
            r -= 1
        else:
            ans.append(l)
            l += 1
    print(" ".join(map(str, ans)))