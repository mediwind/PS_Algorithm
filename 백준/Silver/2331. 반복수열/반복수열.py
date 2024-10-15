def counting(num):
    n = len(str(num))
    
    res = 0
    ten = 10 ** (n - 1)
    while ten:
        res += (num // ten) ** P
        num %= ten
        ten //= 10
    
    return res


A, P = map(int, input().split())
dictionary = {A}
arr = [A]
while True:
    tmp = counting(arr[-1])
    if not tmp in arr:
        arr += [tmp]
    else:
        target = tmp
        break

cnt = 0
for a in arr:
    if a == target:
        break
    cnt += 1
print(cnt)