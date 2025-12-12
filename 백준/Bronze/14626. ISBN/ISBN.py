ISBN = list(input())
res = 0
pos = None
for i in range(12):
    if ISBN[i].isdigit():
        num = int(ISBN[i])
        if i % 2:
            res += num * 3
        else:
            res += num
    else:
        pos = i % 2

res += int(ISBN[-1])

res %= 10
if pos:  # 계수가 3인 경우
    ans = 0
    for d in range(10):
        if (res + 3 * d) % 10 == 0:
            ans = d
            break
else:  # 계수가 1인 경우
    ans = (10 - res) % 10

print(ans)