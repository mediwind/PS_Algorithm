import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    dishes = list(map(int, input().split()))
    
    dishes.sort(reverse=True)
    a, b, c = dishes[0], dishes[1], dishes[2]
    
    ans = 0
    
    if a > 0:
        a -= 1
        ans += 1
    if b > 0:
        b -= 1
        ans += 1
    if c > 0:
        c -= 1
        ans += 1
        
    if a > 0 and b > 0:
        a -= 1
        b -= 1
        ans += 1
    if a > 0 and c > 0:
        a -= 1
        c -= 1
        ans += 1
    if b > 0 and c > 0:
        b -= 1
        c -= 1
        ans += 1
        
    if a > 0 and b > 0 and c > 0:
        a -= 1
        b -= 1
        c -= 1
        ans += 1
        
    print(ans)