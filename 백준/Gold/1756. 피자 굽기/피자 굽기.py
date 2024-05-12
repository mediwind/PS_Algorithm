D, N = map(int,input().split())
oven = list(map(int, input().split()))
pizza = list(map(int,input().split()))

for i in range(len(oven) - 1):
    if oven[i] < oven[i + 1]:
        oven[i + 1] = oven[i]

res = 0 
oven_idx = len(oven) - 1
level = 0

for p in pizza:
    while oven_idx >= 0:
        if p <= oven[oven_idx]:
            res = oven_idx
            oven_idx -= 1
            level += 1
            break
        else:
            oven_idx -= 1

if level == len(pizza):
    print(res + 1)
else:
    print(res)