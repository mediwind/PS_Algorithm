import sys
input = sys.stdin.readline
 
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    
    odds = []
    for ch in s:
        if ch in '13579':
            odds.append(ch)
            if len(odds) == 2:
                break
    
    if len(odds) < 2:
        print(-1)
    else:
        print(odds[0] + odds[1])