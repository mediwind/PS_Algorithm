import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, m, sx, sy = map(int, input().split())
    print(1, 1, n, m)