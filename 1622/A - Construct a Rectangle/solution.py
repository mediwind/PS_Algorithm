import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    sticks = list(map(int, input().rstrip().split()))
    sticks.sort()
    
    a, b, c = sticks
    
    if (a == b and c % 2 == 0) or (b == c and a % 2 == 0) or (a == c and b % 2 == 0):
        print("YES")
    elif a + b == c:
        print("YES")
    else:
        print("NO")