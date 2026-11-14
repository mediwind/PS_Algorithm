import sys
input = sys.stdin.readline
 
n = int(input().strip())
a = list(map(int, input().split()))
 
a.sort()
 
half = n // 2
y = sum(a[:half])
 
x = sum(a[half:])
 
print(x * x + y * y)