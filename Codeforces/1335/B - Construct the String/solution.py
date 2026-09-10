import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    
    ans = [chr(ord('a') + (i % b)) for i in range(n)]
    
    print("".join(ans))