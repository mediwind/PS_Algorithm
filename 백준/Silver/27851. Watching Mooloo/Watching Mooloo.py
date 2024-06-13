n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

answer = 0
for i in range(n):
    if i == 0:
        answer += k + 1
    else:
        extension = arr[i] - arr[i - 1]
        new = k + 1
        answer += min(extension, new)

print(answer)