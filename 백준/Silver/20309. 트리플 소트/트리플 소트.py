n = int(input())
arr = list(map(int, input().split()))

flag = True
for i in range(n):
    if (i % 2 and not arr[i] % 2) or (not i % 2 and arr[i] % 2):
        continue
    flag = False

if flag:
    print("YES")
else:
    print("NO")