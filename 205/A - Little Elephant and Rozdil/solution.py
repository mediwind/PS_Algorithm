import sys
input = sys.stdin.readline
 
n = int(input().strip())
a = list(map(int, input().split()))
 
min_val = min(a)
 
if a.count(min_val) > 1:
    print("Still Rozdil")
else:
    print(a.index(min_val) + 1)