import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    s = input().rstrip()
    n = len(s)
    
    lt = 0
    rt = n - 1
    
    is_alphabetical = True
    
    for i in range(n - 1, -1, -1):
        target_char = chr(ord('a') + i)
        
        if s[lt] == target_char:
            lt += 1
        elif s[rt] == target_char:
            rt -= 1
        else:
            is_alphabetical = False
            break
    
    if is_alphabetical:
        print("YES")
    else:
        print("NO")