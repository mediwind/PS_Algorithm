import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    
    count = n // 2 + 1
    
    print(s // count)