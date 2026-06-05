import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    s = input().rstrip()
    
    ans = ''
    for c in s:
        if c =='L':
            ans += 'L'
        elif c == 'R':
            ans += 'R'
        elif c == 'U':
            ans += 'D'
        else:
            ans += 'U'
    
    print(ans)