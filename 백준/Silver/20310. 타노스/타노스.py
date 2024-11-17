s = input()
n = len(s)
zero = s.count('0')
one = n - zero
zero, one = zero // 2, one // 2

res = ""
for i in range(n):
    if s[i] == '1' and one > 0:
        one -= 1
        continue
    res += s[i]
res = res[::-1]

ans = ""
for i in range(len(res)):
    if res[i] == '0' and zero > 0:
        zero -= 1
        continue
    ans += res[i]

print(ans[::-1])