import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
 
arr = [0]
start = 1
i = 1
while len(arr) <= 1001:
    if (i % 3) and str(i)[-1] != '3':
        arr.append(i)
        start += 1
    i += 1
 
for _ in range(t):
    n = int(input().rstrip())
    print(arr[n])