from math import sqrt


def counting(x):
    cnt = 0
    for i in range(2, int(sqrt(x)) + 1):
        while x % i == 0:
            cnt += 1
            x //= i
    
    if x != 1:
        cnt += 1
        
    return cnt


a, b = map(int, input().split())

nums = [True for _ in range(b + 1)]
nums[1] = False

for i in range(2, b + 1):
    if not nums[i]:
        continue
        
    for j in range(i ** 2, b + 1, i):
        nums[j] = False

ans = 0
for i in range(a, b + 1):
    if nums[counting(i)]:
        ans += 1

print(ans)