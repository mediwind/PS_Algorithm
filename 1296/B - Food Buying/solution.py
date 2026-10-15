import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    s = int(input())
    print(s + (s - 1) // 9)