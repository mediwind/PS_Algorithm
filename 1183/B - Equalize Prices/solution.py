import sys
input = sys.stdin.readline
 
q = int(input().strip())
 
for _ in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    min_a = min(a)
    max_a = max(a)
    
    if min_a + k < max_a - k:
        print(-1)
    else:
        print(min_a + k)