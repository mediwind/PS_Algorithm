import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().strip()
    
    if s[0] == s[-1]:
        print("NO")
        continue
        
    first_char = s[0]
    last_char = s[-1]
    
    remaining_chars = {'A', 'B', 'C'} - {first_char, last_char}
    mid_char = remaining_chars.pop()
    
    is_valid = False
    
    for mid_val in ['(', ')']:
        mapping = {
            first_char: '(',
            last_char: ')',
            mid_char: mid_val
        }
        
        bal = 0
        ok = True
        for ch in s:
            if mapping[ch] == '(':
                bal += 1
            else:
                bal -= 1
                
            if bal < 0:
                ok = False
                break
                
        if ok and bal == 0:
            is_valid = True
            break
            
    if is_valid:
        print("YES")
    else:
        print("NO")