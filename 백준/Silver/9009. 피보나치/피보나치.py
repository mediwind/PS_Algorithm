arr = [0, 1]
for i in range(2, 50):
    arr.append(arr[i - 2] + arr[i - 1])
arr.sort(reverse = True)

t = int(input())
for _ in range(t):
    n = int(input())
    res = list()
    for num in arr:
        if num <= n:
            n -= num
            res.append(num)

    print(*res[:-1:][::-1])