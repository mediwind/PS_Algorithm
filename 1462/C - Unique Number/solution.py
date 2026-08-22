import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    x = int(input())
    
    if x < 10:
        print(x)
        continue
    
    if x > 45:
        print(-1)
        continue
    
    ans = ''
    for i in range(9, 0, -1):
        if x < i:
            continue
        
        ans += str(i)
        x -= i
    
    print(int(ans[::-1]))