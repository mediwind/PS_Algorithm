n = int(input())

cows = list()
for _ in range(n):
    x, y = map(int, input().split())
    cows.append([y, x])

cows.sort()
# cows

lt, rt = 0, len(cows) - 1
ans = float('-inf')

while lt <= rt:
    sub = min(cows[lt][1], cows[rt][1])
    ans = max(ans, cows[lt][0] + cows[rt][0])
    
    if lt == rt:
        sub /= 2
    
    cows[lt][1] -= sub
    cows[rt][1] -= sub
    
    if cows[lt][1] == 0:
        lt += 1
    if cows[rt][1] == 0:
        rt -= 1

print(ans)