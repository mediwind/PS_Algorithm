import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    s = input()
    
    if b > 0:
        print(n * a + n * b)
    else:
        m = 1
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                m += 1
        print(n * a + (m // 2 + 1) * b)