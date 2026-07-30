import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    total_time = a + 2 * b + 3 * c
    
    print(total_time % 2)