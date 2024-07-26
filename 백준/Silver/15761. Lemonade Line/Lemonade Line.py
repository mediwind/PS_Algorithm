n = int(input())
cows = list(map(int, input().split()))
cows.sort(reverse = True)

answer = 0
for i in range(n):
    if i <= cows[i]:
        answer += 1
    else:
        break

print(answer)