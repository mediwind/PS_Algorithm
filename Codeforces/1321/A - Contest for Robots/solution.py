import sys
input = sys.stdin.readline
 
n = int(input())
r = list(map(int, input().split()))
b = list(map(int, input().split()))
 
c_r = 0
c_b = 0
 
for i in range(n):
    if r[i] == 1 and b[i] == 0:
        c_r += 1
    elif r[i] == 0 and b[i] == 1:
        c_b += 1
 
if c_r == 0:
    print(-1)
else:
    print((c_b // c_r) + 1)