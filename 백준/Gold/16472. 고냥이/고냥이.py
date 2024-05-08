n = int(input())
s = input()
length = len(s)

hashing = set()
ans = float('-inf')
lt, rt = 0, 0
while lt < length - 1:
    if rt == length:
        ans = max(ans, rt - lt)
        break
    hashing.add(s[rt])
    if len(hashing) == n:
        ans = max(ans, rt - lt + 1)
        rt += 1
    elif len(hashing) > n:
        lt += 1
        hashing = {s[lt]}
        rt = lt
    else:
        rt += 1
print(ans)