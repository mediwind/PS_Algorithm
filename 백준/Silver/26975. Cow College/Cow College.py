n = int(input())
cows = list(map(int, input().split()))
cows.sort()

ans = 0
tuition = 0
for cow in cows:
    money = n * cow
    if money > ans:
        ans = money
        tuition = cow
    n -= 1

print(ans, tuition)