n = int(input())
ans = ""
while n:
    r = n % 2
    ans += str(r)
    n //= 2
    n *= -1

if not ans:
    print('0')
else:
    print(ans[::-1])