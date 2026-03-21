import sys
input = sys.stdin.readline

q = int(input().strip())

for _ in range(q):
    s = input().strip()
    n = len(s)
    
    if n < 3:
        print(-1)
        continue
        
    min_replace = float('inf')
    
    for i in range(n - 2):
        sub = s[i:i+3]
        
        if sub[1] == 'O':
            if sub == "MOO":
                min_replace = min(min_replace, 0)
            elif sub == "MOM" or sub == "OOO":
                min_replace = min(min_replace, 1)
            elif sub == "OOM":
                min_replace = min(min_replace, 2)
                
    if min_replace == float('inf'):
        print(-1)
    else:
        print((n - 3) + min_replace)