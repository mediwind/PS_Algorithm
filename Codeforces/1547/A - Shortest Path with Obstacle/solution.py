import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    input().rstrip()
    
    xA, yA = map(int, input().rstrip().split())
    xB, yB = map(int, input().rstrip().split())
    xF, yF = map(int, input().rstrip().split())
    
    ans = abs(xA - xB) + abs(yA - yB)
    
    if xA == xB and xA == xF and min(yA, yB) < yF < max(yA, yB):
        ans += 2
    elif yA == yB and yA == yF and min(xA, xB) < xF < max(xA, xB):
        ans += 2
    
    print(ans)