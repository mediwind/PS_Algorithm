import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    
    if B == 1:
        print("NO")
    else:
        print("YES")
        print(A, A * (2 * B - 1), A * 2 * B)