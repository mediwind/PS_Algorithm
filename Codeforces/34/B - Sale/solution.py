import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
a = list(map(int, input().split()))
 
a.sort()
 
total_earnings = 0
 
for i in range(m):
    if a[i] < 0:
        total_earnings += -a[i]
    else:
        break
 
print(total_earnings)