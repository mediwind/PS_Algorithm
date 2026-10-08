import sys
input = sys.stdin.readline
 
n = int(input())
a = list(map(int, input().split()))
 
max_len = 1
current_len = 1
 
for i in range(1, n):
    if a[i] >= a[i - 1]:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 1
 
print(max_len)