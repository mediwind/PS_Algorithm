import bisect

n = int(input())
arr = list(map(int, input().split()))

dy = list()
for i in range(n):
    num = arr[i]
    pos = bisect.bisect_left(dy, num)
    if pos < len(dy):
        dy[pos] = num
    else:
        dy.append(num)

print(len(dy))