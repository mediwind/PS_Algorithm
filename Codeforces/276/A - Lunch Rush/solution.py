import sys
input = sys.stdin.readline
 
n, k = map(int, input().split())
 
max_joy = -float('inf')
 
for _ in range(n):
    f, t = map(int, input().split())
    if t > k:
        joy = f - (t - k)
    else:
        joy = f
    
    if joy > max_joy:
        max_joy = joy
 
print(max_joy)