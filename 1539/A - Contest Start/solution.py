import sys
 
input = sys.stdin.readline
 
q = int(input())
for _ in range(q):
    n, x, t = map(int, input().split())
    
    k = min(n, t // x)
    front_sum = (n - k) * k
    back_sum = k * (k - 1) // 2
    
    print(front_sum + back_sum)