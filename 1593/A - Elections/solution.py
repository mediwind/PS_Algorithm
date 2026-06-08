import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    ans_a = max(0, max(b, c) + 1 - a)
    ans_b = max(0, max(a, c) + 1 - b)
    
    ans_c = max(0, max(a, b) + 1 - c)
    print(ans_a, ans_b, ans_c)