import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())
    
    common = min(p1, p2)
    p1 -= common
    p2 -= common
    
    if p1 >= 7:
        print('>')
    elif p2 >= 7:
        print('<')
    else:
        val1 = x1 * (10 ** p1)
        val2 = x2 * (10 ** p2)
        
        if val1 > val2:
            print('>')
        elif val1 < val2:
            print('<')
        else:
            print('=')