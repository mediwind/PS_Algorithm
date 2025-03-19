from bisect import bisect_left

n = int(input())
lines = list(map(int, input().split()))

dy = list()

for i in range(n):
    port = lines[i]
    pos = bisect_left(dy, port)
    
    if pos < len(dy):
        dy[pos] = port
    else:
        dy.append(port)

print(len(dy))