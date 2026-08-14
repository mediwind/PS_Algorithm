import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    
    if all(ch == '?' for ch in s):
        for i in range(n):
            s[i] = 'B' if i % 2 == 0 else 'R'
    else:
        first_idx = 0
        for i in range(n):
            if s[i] != '?':
                first_idx = i
                break
        
        for i in range(first_idx - 1, -1, -1):
            s[i] = 'R' if s[i + 1] == 'B' else 'B'
            
        for i in range(first_idx + 1, n):
            if s[i] == '?':
                s[i] = 'R' if s[i - 1] == 'B' else 'B'
                
    print(''.join(s))