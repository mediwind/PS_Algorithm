import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    diff = abs(a - b)
    ans = 0
    for i in range(10, 0, -1):
        quotient = diff // i
        diff %= i
        ans += quotient
 
    print(ans)